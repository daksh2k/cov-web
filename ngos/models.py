from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Ngos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    registration_no = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='certificates/%Y/%m/%d/', blank=True)
    website = models.CharField(max_length=200, blank = True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# @receiver(post_save, sender=User)
# def create_ngo_profile(sender, instance, created, **kwargs):
#     if created:
#         ngo = Ngos(user=instance)
#         ngo.save()





