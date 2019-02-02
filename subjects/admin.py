from django.contrib import admin

# Register your models here.
from .models import Subjects, Syllabus, Topics_today
admin.site.register(Subjects)
admin.site.register(Syllabus)
admin.site.register(Topics_today)
