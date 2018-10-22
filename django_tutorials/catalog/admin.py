from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)



class AuthorAdmin (admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Configure entry form. Items in each tuple show on the same row.
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]



admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    """ Creates inline (nested form). """
    extra = 0   # show no additional records for the inlines table. default = 3.
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Slightly different way of registering a model with a class."""

    def display_genre(self, obj):
        """ Create a string for the Genre. This is required to display genre in Admin.
            Note how you use obj here to pull the data.
        """
        return ', '.join(genre.name for genre in obj.genre.all()[:3])      # - Pick top 3 genres for the book.

    display_genre.short_description = 'Genre'
    list_display = ('title', 'author', 'display_genre')

    # Adds the inline :
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """"""
    def get_book_title(self, obj):
        """ Function that gets an attribute through a foreign key. Note the use of the 'obj' parameter!!!
            PARAMETER: self, obj
        """
        return obj.book.title

    get_book_title.short_description = 'Book Title'
    list_display = ('id', 'get_book_title', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

    # fieldsets configures sections in the form and provide heading for each:
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
