from django.contrib import admin

# Register your models here.
from .models import Aspiration, Behavior

admin.site.register(Aspiration)
admin.site.register(Behavior)
