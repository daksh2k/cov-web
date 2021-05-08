from django.db import models
from datetime import datetime
from users.models import Users
from ngos.models import Ngos

class Donation(models.Model):
    users = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    ngos = models.ForeignKey(Ngos, on_delete=models.DO_NOTHING, blank=True, null = True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name


