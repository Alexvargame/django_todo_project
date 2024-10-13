from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import ToDoItem
from .forms import ToDoItemForm

def index_view(request):
    todo_items = ToDoItem.objects.all()
    return render(request, template_name='todo_list/index.html', context={'todo_items': todo_items})

# class ToDoListIndexView(TemplateView):
#     template_name = 'todo_list/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['todo_items'] = ToDoItem.objects.all()
#         return context

class ToDoListIndexView(ListView):
    template_name = 'todo_list/index.html'
    queryset = ToDoItem.objects.all()[:3]

class ToDoListDoneView(ListView):
    #template_name = 'todo_list/index.html'
    queryset = ToDoItem.objects.filter(done=True)

class ToDoListView(ListView):
    model = ToDoItem

class ToDoDetailView(DetailView):
    model = ToDoItem

class ToDoItemCreateVieww(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm


