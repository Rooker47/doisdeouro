from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),

    path('usuarios/', include('appUsuarios.urls'), name='usuarios'),
]
