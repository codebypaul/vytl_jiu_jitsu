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
    instance.badges.save()    

class Membership(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_paid = models.DateField()
    membership_paid=models.IntegerField(blank=True,null=True)



