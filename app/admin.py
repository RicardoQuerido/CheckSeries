from django.contrib import admin

# Register your models here.
from app.models import UserAccount, Episode, Season, TVShow

admin.site.register(TVShow)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(UserAccount)
