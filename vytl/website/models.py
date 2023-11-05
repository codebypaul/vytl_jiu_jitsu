from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class New(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    headline = models.CharField(max_length=200)
    article = models.TextField()
    event_over = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    
    def __str__(self):
        return self.headline
    
    class Meta:
        ordering = ['created']