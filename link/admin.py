from django.contrib import admin
from .models import Link, ClickCount
# Register your models here.

admin.site.register(Link)
admin.site.register(ClickCount)