from django.contrib import admin
from home.models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "date", "todo_image", "is_greater_priority", "profile", )
	list_filter = ("date", "title",)
	search_fields = ("title", "date",)
	