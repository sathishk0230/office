from django.contrib import admin
from . import models

admin.site.register(models.Office)
admin.site.register(models.Employee)
admin.site.register(models.Visitor)
