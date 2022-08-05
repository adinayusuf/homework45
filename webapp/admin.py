from django.contrib import admin

# Register your models here.

from webapp.models import ToDoList, Status, Type, Project


# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = ['id', 'summary', 'status', 'created_at']
#     list_filter = ['summary']
#     list_display_links = ['summary']
#     search_fields = ['summary', 'status']
#     fields = ['summary', 'status', 'type', 'project']


admin.site.register(ToDoList)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)