from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('logout', views.logout_view, name='logout_view'),
    path('add/', views.addTodo, name='add'),
    path('complete/<int:todo_id>', views.completeTodo, name='complete_todo'),
    path('deletecompleted/', views.deleteCompleted, name='delete_completed'),
    path('deleteall/', views.deleteAll, name='delete_all'),
    path('deleteselected/', views.deleteSelected, name='delete_selected')
]