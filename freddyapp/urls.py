# Rutas de la aplicación
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.animatronic_list, name='animatronic_list'),
    path('new', views.animatronic_new, name='animatronic_new'),
    path('<int:id>/view', views.animatronic_view, name='animatronic_view'),
    path('<int:id>/edit', views.AnimatronicUpdate.as_view(), name='animatronic_edit'),
    path('<int:id>/delete', views.AnimatronicDelete.as_view(), name='animatronic_delete'),
    path('newuser', views.register, name='register'),
    path('login', views.FreddyLoginView.as_view(), name='login'),
    path('logout', views.FreddyLogoutView.as_view(), name='logout'),
    path('theme', views.set_dark_theme, name='set_dark_theme'),
    path('clearcookies', views.clear_theme, name='clear_theme'),
]
