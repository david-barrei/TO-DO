from django.shortcuts import render

# Create your views here.

#Crear los login con validaciones por correo electronico
# Enviar mensajes por correo electronico al usuario
#hacer un chat en la aplicacion

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'