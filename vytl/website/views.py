from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.urls import reverse_lazy
# Authentication
from django.contrib.auth.views import LoginView
# Create your views here.

# General site pages
def home_view(request):
    return render(request, 'pages/home.html', context = {}, status =200 )

def schedule(request):
    return render(request, 'pages/schedule.html', context = {}, status =200 )


# Authentication pages
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home page')
    
# Authenticated user pages
def profile(request):
    return render(request, 'user/profile.html')
# Admin pages
