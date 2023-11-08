from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

# Authentication
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

from customadmin.models import Attend

# Pagination
from django.core.paginator import Paginator

# Create your views here.

# General site pages
def home_view(request):
    return render(request, 'pages/home.html', context = {}, status =200 )

def schedule(request):
    return render(request, 'pages/schedule.html', context = {}, status = 200 )

def about(request):
    return render(request, 'pages/about.html', context = {}, status = 200) 

def instructors(request):
    return render(request, 'pages/instructors.html', context = {}, status = 200 )

def pricing(request):
    return render(request, 'pages/pricing.html', context = {}, status = 200 )


# Authentication pages
class RegisterPage(FormView):
    template_name =  'auth/register.html' 
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user =form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home view')
        return super(RegisterPage,self).get(*args,**kwargs)
    
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home page')
    
# Authenticated user pages
def profile(request):
    user=request.user
    attendance=Attend.objects.filter(student=user).order_by('class_date')
    context={
        'attendance':attendance,
    }
    return render(request, 'user/profile.html',context=context,status=200)

