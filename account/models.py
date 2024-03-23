from django.db import models
from django.contrib.auth.models import User
class adminActount(models.Model):
    admin_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.admin_name