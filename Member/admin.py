from django.contrib import admin
from .models import Country, State, City, Job, Member

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Job)
admin.site.register(Member)