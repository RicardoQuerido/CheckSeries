from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class TVShow(models.Model):
    tv_id = models.IntegerField
    is_checked = models.BooleanField

    def __str__(self):
        return self.tv_id


class Season(models.Model):
    number = models.IntegerField
    is_checked = models.BooleanField
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Episode(models.Model):
    number = models.IntegerField
    is_checked = models.BooleanField
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(TVShow)

    def __str__(self):
        return self.user.username
