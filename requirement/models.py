from django.db import models
from ngos.models import Ngos

class Requirement(models.Model):
    ngos = models.ForeignKey(Ngos, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_satisfied = models.BooleanField(default=False)
    def __str__(self):
        return self.name

