from django.contrib import admin

# Register your models here.

from .models import Candidate, PoliticalCoalition

admin.site.register(Candidate)
admin.site.register(PoliticalCoalition)
