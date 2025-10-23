from django.contrib import admin
from .models import Dish
from .models import Course
from .models import Ingredient


admin.site.register(Dish)
admin.site.register(Course)
admin.site.register(Ingredient)

