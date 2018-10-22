import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Book, Author, BookInstance, Genre
from .forms import RenewBookForm


# Create your views here.

@login_required
def index(request):
    """ View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


@method_decorator(login_required, name='dispatch')
class BookListView(generic.ListView):
    """ Create generic list view on the Book model."""
    model = Book
    paginate_by = 10
    # Simple way to override default data:
    context_object_name = 'my_book_list'    # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5]      # Get 5 books containing the title war
    template_name = 'books/book_list.html'    # Specify your own template name/location

    def get_queryset(self):
        """Another way to override the query set. This one is more flexible..."""
        return Book.objects.all()     # Get 5 books containing the title war.

    def get_context_data(self, **kwargs):
        """ We might also override get_context_data() in order to pass additional context variables to the template
            (e.g. the list of books is passed by default). The fragment below shows how to add a variable named
            "some_data" to the context (it would then be available as a template variable).

            When doing this it is important to follow the pattern used below:
            1) First get the existing context from our superclass.
            2) Then add your new context information.
            3) Then return the new (updated) context.
        """
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


@method_decorator(login_required, name='dispatch')
class BookDetailView(generic.DetailView):
    model = Book


@method_decorator(login_required, name='dispatch')
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'my_author_list'
    template_name = 'authors/author_list.html'


@method_decorator(login_required, name='dispatch')
class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        """ Query for books that are 'on loan' and are borrowed by User. Order by due back. """
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin,generic.ListView):
    """
    Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission.
    """
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
#@permission_required('catalog.can_edit')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        book_renewal_form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if book_renewal_form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = book_renewal_form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('catalog:all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        book_renewal_form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
    'form': book_renewal_form,
    'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


# Generic views / forms that add/update/delete records. You can use for habits, exercises etc.

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')