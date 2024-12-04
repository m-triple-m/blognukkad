from django.contrib import admin
from martor.widgets import AdminMartorWidget
from .models import Blog

# Register your models here.
admin.site.register(Blog)