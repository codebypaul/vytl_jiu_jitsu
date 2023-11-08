from django.urls import path
from . import views

urlpatterns= [

    path('dashboard/',views.admin_panel,name='admin panel'),
    path('students/',views.admin_students, name ='admin students'),
    path('attendance/',views.attendance, name ='attendance'),
    
]