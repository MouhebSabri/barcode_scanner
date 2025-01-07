from django.urls import path
from .views import scan_page, scan_barcode

urlpatterns = [
    path('scan/', scan_page, name='scan_page'),  # Route pour afficher la page avec la caméra
    path('scan/<str:barcode>/', scan_barcode, name='scan_barcode'),  # Route pour traiter un code-barres
]
