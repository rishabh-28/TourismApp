from django.contrib import admin
from .models import *

admin.site.register(state)
admin.site.register(city)
admin.site.register(place)
admin.site.register(rating)
admin.site.register(support)