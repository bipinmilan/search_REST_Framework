from django.contrib import admin

# Register your models here.
from Chained.models import Country, City, Person


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
