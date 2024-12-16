from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')
    prepopulated_fields = {"slug": ("name", )}  

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(AdvancedProfile)
admin.site.register(OrdinaryProfile)
admin.site.register(Commentary)




