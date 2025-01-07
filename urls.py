from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/scan/')),  # Rediriger le chemin racine vers /scan/
    path('', include('scanner.urls')),  # Inclure les routes de l'application scanner
]