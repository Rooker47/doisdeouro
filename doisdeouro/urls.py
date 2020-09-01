from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(r'^admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('cadastrar/', include('appCadastros.urls'), name='cadastrar'),
    path('listar/', include('appListas.urls'), name='listar'),
]
