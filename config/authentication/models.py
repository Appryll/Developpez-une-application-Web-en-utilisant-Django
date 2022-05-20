from django.db import models
from django.contrib.auth.models import User #table user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='static/img_default.png')

    def __str__(self):
        return f'Profile de {self.user.username}'

