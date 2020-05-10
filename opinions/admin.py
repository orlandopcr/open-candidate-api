from django.contrib import admin

# Register your models here.
from opinions.models import KeyTopic, Tag, Opinion

admin.site.register(KeyTopic)
admin.site.register(Tag)
admin.site.register(Opinion)
