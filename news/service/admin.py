from django.contrib import admin
from service.models import service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('topic','image','writer','Date','Headline','info')


admin.site.register(service,ServiceAdmin)

# Register your models here.
