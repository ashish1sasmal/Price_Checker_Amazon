from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.user.email}'

class Products(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    url = models.URLField()
    title = models.TextField(default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self):
        return f'{self.user.email} {self.title[:40]}'

class ControlRoom(models.Model):
    interval = models.IntegerField()

    def __str__(self):
        return f'Interval = {self.interval}'
