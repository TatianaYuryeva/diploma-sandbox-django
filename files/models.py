from django.db import models
from django.contrib.auth.models import User
from django.template.backends import django


def user_directory_path(instance):
    return f'{User.username}'


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    size = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    download_last_date = models.DateTimeField(null=True)
    comment = models.TextField(max_length=120, blank=True)
    path = models.CharField(null=True)
    download_link = models.CharField(null=True)
    upload = models.FileField(upload_to='test/')
    # user_id = models.IntegerField(default=0)


