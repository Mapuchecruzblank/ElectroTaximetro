from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('app/', views.dashboard, name='dashboard'),
    path('app/toggle/<int:dispositivo_id>/', views.toggle_dispositivo, name='toggle_dispositivo'),
    path('app/eliminar/<int:dispositivo_id>/', views.eliminar_dispositivo, name='eliminar_dispositivo'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name='sw'),
]