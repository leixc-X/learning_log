from django.contrib import admin

# Register your models here.

from learning_logs.models import Topci, Entry

admin.site.register(Topci)
admin.site.register(Entry)