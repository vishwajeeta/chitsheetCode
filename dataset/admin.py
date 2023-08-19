from django.contrib import admin
from .models import sample
# Register your models here.
class regesterAdmin(admin.ModelAdmin):
    list_display=['topic','language']
admin.site.register(sample,regesterAdmin)
admin.site.site_header="chartSheet Management"