from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns =  [
    # General site pages
    path('',views.home_view, name = 'home page'),
    path('schedule',views.schedule, name = 'schedule'),
    # path('about/',views.about,name='about'),
    # Authentication
    path('',views.home_view, name = 'sign-up'),
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(next_page='home page'), name = 'logout'),
    # Authenticated user pages
    path('profile/',views.profile, name = 'profile'),



]