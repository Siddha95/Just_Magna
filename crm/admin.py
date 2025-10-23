from django.contrib import admin
from .models import Survey
from .models import Rating

# Register your models here.
admin.site.register(Survey)
admin.site.register(Rating)