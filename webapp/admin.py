from django.contrib import admin

# Register your models here.

from webapp.models import To_do_list



class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['description']
    list_display_links = ['description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'text', 'date_of_completion']
    readonly_fields = ['date_of_completion']



admin.site.register(To_do_list,ToDoListAdmin)