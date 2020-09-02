from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='appUsuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appUsuarios/logout.html'), name='logout'),
    path('', UsuarioCreate.as_view(), name='registrar'),
]