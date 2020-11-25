from django.urls import path
from home.views import home_view, add_todo, update_todo, delete_todo

app_name = "home"

urlpatterns = [
    path('todo_list/', home_view, name='todo_list'),
    path('add_todo/', add_todo, name='add_todo'),
    path('update_todo/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'),
] 
