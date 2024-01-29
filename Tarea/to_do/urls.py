from django.urls import path
from . import views

app_name= "todo_app"


urlpatterns = [
    path('task/',views.TareaView.as_view(),name='tarea'),
    path('add-task/',views.AddTaks.as_view(),name='add-task'),
    path('list-task/',views.TareaList.as_view(),name='task'),
    path('delete-task/<int:pk>/',views.TareaDelete.as_view(),name='delete'),

]
