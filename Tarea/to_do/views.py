from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView, DeleteView, UpdateView
from  .models import TaskModel
from .forms import AddForm
# Create your views here.
#Creando un nuevo modelo
class HomeView(TemplateView):
    template_name = 'home.html'


class AddTaks(CreateView):
    form_class = AddForm
    template_name = 'add-taks.html'
    tasks = TaskModel.objects.all()
    success_url = '.'
    #


class TareaList(ListView):
    template_name = "list-taks"
    context_object_name = 'tasks'


    def get_queryset(self):
        return TaskModel.objects.all()
    
class TareaEdit(UpdateView):
    template_name = 'edit.html'
    model = TaskModel
    form_class = AddForm
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********post******')
        responde = super().post(request, *args, **kwargs)
        return HttpResponseRedirect(self.get_success_url())
        

    def form_valid(self, form):
        print("El método form_valid se está ejecutando")
        if form.is_valid():
            print("El formulario es válido")
        else:
            print("El formulario no es válido")
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('todo_app:task')

   

class TareaDelete(DeleteView):
    model = TaskModel
    template_name = 'index.html'
    success_url = reverse_lazy('todo_app:task')
