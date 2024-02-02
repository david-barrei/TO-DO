from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name= "todo_app"


urlpatterns = [
    path('task/',views.TareaView.as_view(),name='tarea'),
    path('add-task/',views.AddTaks.as_view(),name='add-task'),
    path('list-task/',views.TareaList.as_view(),name='task'),
    path('delete-task/<int:pk>/',views.TareaDelete.as_view(),name='delete'),
    path('edit-task/<int:pk>/',views.TareaEdit.as_view(),name='edit'),

] 
