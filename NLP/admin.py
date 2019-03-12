from django.contrib import admin

# Register your models here.

from .models import NLP_MAPS, Organisation

admin.site.register(NLP_MAPS)
admin.site.register(Organisation)
