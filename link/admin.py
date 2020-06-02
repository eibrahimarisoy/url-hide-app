from django.contrib import admin
from .models import Link, Click, Browser, OperatingSystem
# Register your models here.

admin.site.register(Link)
admin.site.register(Click)
admin.site.register(Browser)
admin.site.register(OperatingSystem)
