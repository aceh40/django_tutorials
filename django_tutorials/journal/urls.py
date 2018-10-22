from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
]


##############################
### - test stuff:
##############################
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('activity/', views.activity, name='activity'),
#     path(r'activity/<int:pk>/', views.activity_detail, name='activity_detail'),
#     path(r'activity/no_sugar/', views.no_sugar, name='no_sugar'),
#     path(r'activity/no_sugar_history/', views.no_sugar_history, name='no_sugar_history'),
# ]