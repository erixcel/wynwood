from django.contrib import admin
from .models import Country, State, City, Property, Reservation, PropertyPhoto, User

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Property)
admin.site.register(PropertyPhoto)
admin.site.register(Reservation)
admin.site.register(User)