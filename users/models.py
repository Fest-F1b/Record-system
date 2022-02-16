from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default..jpg', upload_to='profile_pics/',
                              null=True, blank=True, verbose_name="Profile Picture")

    def __str__(self) -> str:
        return f'{self.user.username} Profile'