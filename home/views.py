from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from home.models import Todo
from home.forms import TodoForm


def home_view(request):

	todos = Todo.objects.all()
	context = {"todos" : todos, "username": request.user}
	return render(request, "todo_list.html", context)

def add_todo(request):
	form = TodoForm(request.POST or None, request.FILES or None)
	context = {"form" : form}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('home:todo_list'))
	return render(request, "form.html", context)

def update_todo(request,todo_id):
	todo = get_object_or_404(Todo,id=todo_id)
	form = TodoForm(request.POST or None, request.FILES or None, instance=todo)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('home:todo_list'))
	return render(request, "form.html", {"form" : form})

def delete_todo(request, todo_id):	# passing the request and POST from the delete key in indext.html
	todo = get_object_or_404(Todo, id=todo_id) 	# getting the item ready which was requested with POST method
	if request.method == 'POST':	# this POST is confirm button in the delete.html page which passes through request 
		todo.delete()	# builtin delete function in django models
		return HttpResponseRedirect(reverse("home:todo_list")) # it will redirect to main page of book list after deletion
	return render(request, "delete.html", {"item" : todo})	# rendering to delete.html page, helps to go through html here
