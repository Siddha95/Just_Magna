from django.contrib import admin
from .models import Dish
from .models import Course
from .models import Ingredient
from rest_framework.authtoken.admin import TokenAdmin



admin.site.register(Dish)
admin.site.register(Course)
admin.site.register(Ingredient)

TokenAdmin.raw_id_fields = ['user']

