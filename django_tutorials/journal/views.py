from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.


def home(request):
    return render(request,'journal/home.html', {})







##############################
### - test stuff:
##############################

# from .models import Activity, NoSugar
# from .forms import NoSugarForm
#
#
# def home(request):
#     return render(request,'journal/index.html', {})
#
#
# def activity(request):
#     """
#     :param request:
#     :return:
#     """
#     activity_list = Activity.objects.filter(active_flag=True).order_by('activity_name')
#     return render(request,'journal/activity.html', {'activity_list': activity_list})
#
#
# def activity_detail(request, pk):
#     activity = get_object_or_404(Activity, pk=pk)
#     return render(request, 'journal/activity_detail.html', {'activity': activity})
#
#
# def no_sugar(request):
#     """ Simple view of no_sugar page
#     """
#     if request.method == 'POST':
#         form = NoSugarForm(request.POST)
#         if form.is_valid():
#             log = form.save(commit=False)
#             log.save()
#             return HttpResponseRedirect(reverse('no_sugar_history'))
#     else:
#         form = NoSugarForm()
#         return render(request, 'journal/no_sugar.html', {'form': form})
#
#
# def no_sugar_history(request):
#     log_list = NoSugar.objects.order_by('entry_date')
#     return render(request, 'journal/no_sugar_history.html', {'logs': log_list})
#