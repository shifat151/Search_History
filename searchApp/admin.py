from django.contrib import admin

from searchApp.models import search_result, Search_detail

# Register your models here.
admin.site.register(search_result)
admin.site.register(Search_detail)
