from django.contrib import admin

from . models import Place
# Register your models here.
admin.site.register(Place)

from . models import explorer

admin.site.register(explorer)