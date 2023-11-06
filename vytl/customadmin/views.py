from django.shortcuts import render, redirect
from django.contrib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin panel')
        # messages.info(request,'Account not found')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            user_obj = authenticate(username=username,password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('admin page')
            
            messages.info(request,'Invalid Password')
            return redirect('home page')
        return render(request, 'auth/login.html')
    except Exception as e:
        print(e)