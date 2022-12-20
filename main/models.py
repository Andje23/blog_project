from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text="Write your blog")
    past_date = models.DateField(default=date.today)