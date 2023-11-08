from django.shortcuts import render, redirect
# Models
from django.contrib.auth.models import User
from .models import Attend, Class
# Authentication
from django.contrib.auth import authenticate, login

# Pagination
from django.core.paginator import Paginator
# Create your views here.

# def admin_login(request):
#     try:
#         if request.user.is_authenticated:
#             return redirect('admin panel')
#         # messages.info(request,'Account not found')
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user_obj = User.objects.filter(username=username)
#             if not user_obj.exists():
#                 messages.info(request, 'Account not found')
#                 return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
#             user_obj = authenticate(username=username,password=password)

#             if user_obj and user_obj.is_superuser:
#                 login(request, user_obj)
#                 return redirect('admin page')
            
#             messages.info(request,'Invalid Password')
#             return redirect('home page')
#         return render(request, 'auth/login.html')
#     except Exception as e:
#         print(e)

# Admin only
def admin_panel(request):
    # User data
    user_list=User.objects.all().order_by('last_name')
    
    user_p=Paginator(User.objects.all().order_by('last_name'),10)
    user_page=request.GET.get('page')
    users=user_p.get_page(user_page)

    context={
        'user_list':user_list,
        'users': users,
    }
    return render(request, 'admin/admin_panel.html',context=context, status = 200)

def admin_students(request):
    # User data
    user_list=User.objects.all().order_by('last_name')
    
    user_p=Paginator(User.objects.all().order_by('last_name'),10)
    user_page=request.GET.get('page')
    users=user_p.get_page(user_page)

    context={
        'user_list':user_list,
        'users': users,
    }
    return render(request, 'admin/students/students_dashboard.html',context=context, status = 200)

def attendance(request):
    attendance_list=Attend.objects.all()
    
    context = {
        'attendance_list':attendance_list,
    }
    return render(request,'admin/students/attendance.html',context=context,status=200)