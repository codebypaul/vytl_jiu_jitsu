from django.contrib import admin
from .models import Profile, Badge, Class, Attend, Membership, Expense, MemberIncome

# Register your models here.
admin.site.register(Profile)
admin.site.register(Badge)
admin.site.register(Class)
admin.site.register(Attend)
admin.site.register(Membership)
admin.site.register(MemberIncome)
admin.site.register(Expense)
