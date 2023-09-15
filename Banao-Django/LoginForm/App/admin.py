from django.contrib import admin
from .models import Person,Blog,Draft,Appointment

admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Draft)
admin.site.register(Appointment)
