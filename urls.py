from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),  # Inclui as URLs do app cadastro
]
