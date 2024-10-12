from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, ListView, DetailView

from .models import ToDoItem

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