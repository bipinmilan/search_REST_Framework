from django.contrib import admin

# Register your models here.
from data.models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('title',)
    search_fields = ('title', 'description', 'name')
    list_per_page = 25


admin.site.register(Data, DataAdmin)
