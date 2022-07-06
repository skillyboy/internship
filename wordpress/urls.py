from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/', views.poll, name='poll'),
    path('profile/', views.profile, name='profile'), 
    
    
    path('signup/', views.signupform, name='signupform'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    
    path('save/', views.save, name='save'),
    path('pollview/', PollView.as_view(), name='pollview'),
    path('axiosview/', AxiosView.as_view(), name='axiosview'),
    path('pollform/', PollFormView.as_view(), name='pollform'),
    
]