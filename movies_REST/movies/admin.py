from django.contrib import admin
from .models import Person, Movie, Role

# Register your models here.
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Role)
