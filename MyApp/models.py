from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.
class Help(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, unique=False)

    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    helpTime = models.DateTimeField(default=timezone.now)
    company = models.CharField(max_length=100, default='--select--')
    c_model = models.CharField(max_length=25, default='model name')
    issue = models.CharField(max_length=25, default='others')
    o_issue = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username
