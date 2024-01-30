from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from  .models import TaskModel
from .forms import AddForm
# Create your views here.

class TareaView(TemplateView):
    template_name = 'index.html'


class AddTaks(CreateView):
    form_class = AddForm
    template_name = 'add-taks.html'
    tasks = TaskModel.objects.all()
    success_url = '.'
    #



class TareaList(ListView):
    template_name = "index.html"
    context_object_name = 'tasks'


    def get_queryset(self):
        return TaskModel.objects.all()

class TareaDelete(DeleteView):
    model = TaskModel
    template_name = 'index.html'
    success_url = reverse_lazy('todo_app:task')
