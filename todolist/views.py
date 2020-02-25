from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models

class TodoIndex(ListView):
    template_name='todolist/index.html'
    model=models.TodoModel

class TodoCreate(CreateView):
    template_name = 'todolist/create.html'
    model = models.TodoModel
    fields = ('title','memo', 'priority', 'duedate')
    success_url = reverse_lazy('todoindex')

class TodoDetail(DetailView):
    template_name = 'todolist/detail.html'
    model = models.TodoModel

class TodoUpdate(UpdateView):
    template_name = 'todolist/update.html'
    model = models.TodoModel
    fields = ('title','memo', 'priority', 'duedate')
    success_url = reverse_lazy('todoindex')

class TodoDelete(DeleteView):
    template_name = 'todolist/delete.html'
    model = models.TodoModel
    success_url = reverse_lazy('todoindex')
