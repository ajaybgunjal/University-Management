from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Advisor)


