from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .models import Todo
from .forms import TodoForm, TodoModelForm

def user_login(request):
	""" User logged in
	"""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
	return render(request, 'auth/login.html', {})

def user_logout(request):
	""" user logout
	"""
	logout(request)
	return redirect('index')


def add_todo(request):
	if not request.user.is_authenticated():
		# dispay 404page if user is not login
		raise Http404
	form = TodoModelForm()
	if request.POST:
		form = TodoModelForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.user = request.user
			todo.save()
			return redirect('detail', pk=todo.id)
	return render(request, 'todo/todo_form.html', {'form': form})


def home(request):
	if request.user.is_authenticated():
		todos = Todo.objects.filter(user=request.user)
	else: 
		todos = Todo.objects.all()
	return render(request, 'todo/home.html', {'todos': todos})


def detail(request, pk):
	if request.user.is_authenticated():
		todo = get_object_or_404(Todo, id=pk, user=request.user)
		return render(request, 'todo/detail.html', {'todo': todo})
	raise Http404

@login_required(login_url='/login')
def update_todo(request, pk):
	"""Updating todo
	"""
	todo = get_object_or_404(Todo, id=pk)
	form = TodoModelForm(instance=todo)
	if request.POST:
		form = TodoModelForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save()
			return redirect('detail', pk=todo.id)
	return render(request, 'todo/todo_form.html', {'form': form})


def delete_todo(request, todo_id):
	""" Delete todo object
	"""
	if request.method == 'POST':
		todo = get_object_or_404(Todo, id=todo_id)
		todo.delete()
		return redirect('index')
	raise Http404()

def mark_complete(request, todo_id):
	todo = get_object_or_404(Todo, id=todo_id)
	todo.is_done = False if todo.is_done else True
	todo.save()
	return redirect('index')

