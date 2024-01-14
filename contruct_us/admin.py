from django.contrib import admin
from.models import ContructUs
# Register your models here.
class ContructModeladmin(admin.ModelAdmin):
    list_display=['name','phone','problem']
admin.site.register(ContructUs, ContructModeladmin)