from django.contrib import admin
from home.models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ("title", "description", "date", "todo_image",)
	list_filter = ("date",)
	search_fields = ("title", "date",)
	