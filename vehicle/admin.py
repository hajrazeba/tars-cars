from django.contrib import admin

# Register your models here.
from vehicle.models import *

admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Request)
admin.site.register(Attendance)
admin.site.register(Feedback)
