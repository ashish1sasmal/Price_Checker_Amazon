from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

class Products(models.Model):
    user = models.ForeignKey(Profile,on_delete = models.CASCADE)
    url = models.URLField()
    title = models.TextField(default='')
    def __str__(self):
        return f'{self.user.email}'
