from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    belt=models.CharField(default='White')
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


class Badge(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    day_one=models.BooleanField(default=False)
    investor=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
@receiver(post_save,sender=User)
def create_user_badges(sender,instance,created,**kwargs):
    if created:
        Badge.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_badges(sender,instance,**kwargs):
    instance.badge.save()    

# 
class Membership(models.Model):
    member_choices = (
        ('Adult Unlimited','Adult Unlimited'),
        ('Kids Unlimited','Kids Unlimited')
    )
    member_costs=(
        (130,130),
        (100,100)
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_paid = models.DateField()
    membership_paid=models.IntegerField(blank=True,null=True,choices=member_costs)

    def __str__(self):
        return f'{self.user} {self.date_paid}'

# Class Models

class Class(models.Model):
    class_time = models.CharField(max_length=50)
    class_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.class_time} | {self.class_name}'

class ClassNote(models.Model):
    sched_class=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    topic=models.CharField()
    class_notes=models.TextField()
    date=models.DateField()

class Attend(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    class_info = models.ForeignKey(Class,on_delete=models.DO_NOTHING,blank=True,null=True)
    class_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.student} - {self.class_date} : {self.class_info}'

# Expenses
class Expense(models.Model):
    expense=models.CharField()
    cost=models.FloatField()
    date_paid=models.DateField()
    paid_to=models.CharField(null=True,blank=True)
    website=models.URLField(null=True,blank=True)

    def __str__(self):
        return f'{self.expense} | {self.date_paid}'
    
    class Meta:
        ordering = ['date_paid','expense']