from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from  .models import TaskModel
from .forms import AddForm
# Create your views here.

class TareaView(TemplateView):
    template_name = 'index.html'


class AddTaks(CreateView):
    form_class = AddForm
    template_name = 'index.html'
    tasks = TaskModel.objects.all()
    success_url = '.'



class TareaList(ListView):
    template_name = "index.html"
    context_object_name = 'tasks'


    def get_queryset(self):
        return TaskModel.objects.all()

