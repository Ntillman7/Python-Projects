from django.contrib import admin
from classApp.models import UniversityClasses
from campusApp.models import UniversityCampus


# Register your models here.
admin.site.register(UniversityClasses)
admin.site.register(UniversityCampus)