from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),

    path('cadastrar/', include('appCreate.urls'), name='cadastrar'),
    path('atualizar/', include('appUpdate.urls'), name='atualizar'),
    path('apagar/', include('appDelete.urls'), name='apagar'),
    path('listar/', include('appListas.urls'), name='listar'),
    path('usuarios/', include('appUsuarios.urls'), name='usuarios'),
    path('almox/', include('appAlmox.urls'), name='almox'),
    path('ssmb/', include('appSsMB.urls'), name='ssmb'),
    path('p1/', include('appPrimeiraSecao.urls'), name='p1'),
]
