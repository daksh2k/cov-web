from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         u = Users(user=instance)
#         u.save()