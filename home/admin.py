from django.contrib import admin
from home.models import career
# Register your models here.

class career(admin.ModelAdmin):
    list_display=['cfirstname','clastname','caddress','cno']
    #admin.site.register[career]