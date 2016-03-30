from django.contrib import admin

from .models import Course, Lecture

admin.site.register(Lecture)
admin.site.register(Course)
# Register your models here.
