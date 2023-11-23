from django.shortcuts import render, redirect
from datetime import date
# Models
from django.contrib.auth.models import User
from .models import Attend, Class, Expense, MemberIncome
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
    # Date
    today_date=date.today()
    # User data
    user_list=User.objects.all().order_by('last_name')
    
    user_p=Paginator(User.objects.all().order_by('last_name'),10)
    user_page=request.GET.get('page')
    users=user_p.get_page(user_page)

    # Membership
    memberships_year=MemberIncome.objects.filter(date_paid__year=today_date.year)
    # memberships_month=Membership.objects.filter(date_paid__month=today_date.month)


    current_month_member_income = 0
    # for x in memberships_month:
    #     current_month_member_income += x.membership_paid
    
    year_member_income = 0
    for x in memberships_year:
        year_member_income += x.user.profile.membership.price

    # Expenses
    expenses_month = Expense.objects.filter(date_paid__month=today_date.month)
    expenses_year = Expense.objects.filter(date_paid__year=today_date.year)

    current_month_expenses = 0
    for x in expenses_month:
        current_month_expenses += x.cost

    current_year_expenses = 0
    for x in expenses_year:
        current_year_expenses += x.cost

    print(request.GET.get('student-quantity-filter'))
    context={
        'user_list':user_list,
        'users': users,

        'date':today_date,
        'month':today_date.strftime('%B'),
        'year':today_date.strftime('%Y'),

        'memberships_year':memberships_year,
        # 'memberships_month':memberships_month,
        'current_month_member_income':current_month_member_income,
        'year_member_income':year_member_income,

        'expenses_month':expenses_month,
        'expenses_year':expenses_year,
        'current_month_expenses':current_month_expenses,
        'current_year_expenses':current_year_expenses,
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
    # search_input=request.GET.get('search-area') or ''

    attendance_list=Attend.objects.values('class_date')
    # .order_by('class_date','class_info','student')

    user_list=User.objects.all().order_by('last_name')

    attend_p=Paginator(Attend.objects.all().order_by('class_date'),10)
    attend_page=request.GET.get('page')
    attends=attend_p.get_page(attend_page)

    context = {
        'attendance_list':attendance_list,
        'user_list':user_list,
        'attends':attends
    }
    return render(request,'admin/students/attendance.html',context=context,status=200)

def memberships(request):
    # Dates
    today_date=date.today()

    # Membership
    member_income_p=Paginator(MemberIncome.objects.filter(date_paid__month=today_date.month),10)
    member_income_page=request.GET.get('page')
    memberships=member_income_p.get_page(member_income_page)

    context={
        # 
        'today':today_date,
        'month':today_date.strftime('%B'),
        'memberships':memberships,
    }
    return render(request,'admin/students/memberships.html',context=context,status=200)