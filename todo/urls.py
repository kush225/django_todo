from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('logout/', views.logout_view, name='logout_view'),
    path('settings/',views.settings,name='settings'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'), name='password_reset_main'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uridb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('add/', views.addTodo, name='add'),
    path('complete/<int:todo_id>', views.completeTodo, name='complete_todo'),
    path('deletecompleted/', views.deleteCompleted, name='delete_completed'),
    path('deleteall/', views.deleteAll, name='delete_all'),
    path('deleteselected/', views.deleteSelected, name='delete_selected')
]