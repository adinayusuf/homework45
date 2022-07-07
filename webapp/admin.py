from django.contrib import admin

# Register your models here.

from webapp.models import ToDoList, Status, Type


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at']
    list_filter = ['summary']
    list_display_links = ['summary']
    search_fields = ['summary', 'status']
    fields = ['summary', 'status', 'type']


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Status)
admin.site.register(Type)
