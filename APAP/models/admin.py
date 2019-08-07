from django.contrib import admin
from models.models import User, University, Lecture, Schedule, Print, PrintRequest

admin.site.register(User)
admin.site.register(University)
admin.site.register(Lecture)
admin.site.register(Schedule)
admin.site.register(Print)
admin.site.register(PrintRequest)
# Register your models here.
