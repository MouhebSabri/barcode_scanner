from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import Product
import logging
from .utils import map_category_to_recycling_type


logger = logging.getLogger(__name__)

API_KEY = "m2cix88kkoh9k07wyjhgscoubwmxlm"

def scan_page(request):
    return render(request, 'scanner/scan.html')

def scan_barcode(request, barcode):
    logger.info(f"Requête reçue avec le code-barres : {barcode}")

    try:
        product = Product.objects.get(barcode=barcode)
        return JsonResponse({
            'name': product.name,
            'category': product.category,
            'brand': product.brand,
            'image_url': product.image_url,
            'recycling_type': product.recycling_type
        })
    except Product.DoesNotExist:
        pass

    api_url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&key={API_KEY}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data.get('products'):
            product_data = data['products'][0]
            recycling_type = map_category_to_recycling_type(product_data.get("category", ""))

            product = Product.objects.create(
                barcode=barcode,
                name=product_data.get("product_name", "Nom indisponible"),
                category=product_data.get("category", "Catégorie indisponible"),
                brand=product_data.get("brand", "Marque indisponible"),
                image_url=product_data.get("images", [""])[0],
                recycling_type=recycling_type
            )
            return JsonResponse({
                'name': product.name,
                'category': product.category,
                'brand': product.brand,
                'image_url': product.image_url,
                'recycling_type': product.recycling_type
            })
        else:
            return JsonResponse({'error': 'Produit non trouvé dans l’API'}, status=404)
    else:
        return JsonResponse({'error': f"Erreur lors de l’appel à l’API : {response.status_code}"}, status=500)
