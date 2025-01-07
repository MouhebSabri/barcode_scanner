from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import Product
import logging

logger = logging.getLogger(__name__)

# Remplacez par votre clé API Barcode Lookup
API_KEY = "m2cix88kkoh9k07wyjhgscoubwmxlm"

def map_category_to_recycling_type(category):
    """
    Mappe une catégorie API à un type de déchet spécifique (français et anglais).
    """
    category = category.lower()

    # Recyclables (emballages, papier/carton)
    if any(keyword in category for keyword in [
        "plastique", "carton", "papier", "emballage", "bouteille", "canette", "alu", "aluminium",
        "plastic", "cardboard", "paper", "packaging", "bottle", "can", "aluminum"
    ]):
        return "Recyclables"

    # Compost (déchets organiques)
    elif any(keyword in category for keyword in [
        "organique", "alimentaire", "compost", "déchet de cuisine", "fruits", "légumes", "épluchures",
        "organic", "food waste", "compostable", "kitchen waste", "fruits", "vegetables", "peelings"
    ]):
        return "Compost"

    # Verre
    elif any(keyword in category for keyword in [
        "verre", "bocal", "bouteille en verre", "pot",
        "glass", "jar", "glass bottle", "container"
    ]):
        return "Verre"

    # Ordures ménagères
    elif any(keyword in category for keyword in [
        "ordures ménagères", "non recyclable", "déchet général", "restes",
        "household waste", "non-recyclable", "general waste", "leftovers"
    ]):
        return "Ordures ménagères"

    # Déchets spéciaux (piles, électronique)
    elif any(keyword in category for keyword in [
        "pile", "batterie", "électronique", "électroménager", "téléphone", "ordinateur", "déchet dangereux",
        "battery", "electronics", "appliance", "phone", "computer", "hazardous waste"
    ]):
        return "Déchets spéciaux"

    # Par défaut, catégorie inconnue
    return "Autre"

def scan_page(request):
    """
    Vue pour rendre la page HTML avec l'interface de scan.
    """
    return render(request, 'scanner/scan.html')

def scan_barcode(request, barcode):
    """
    Vue pour traiter les requêtes d'identification de produit via un code-barres.
    """
    logger.info(f"Requête reçue avec le code-barres : {barcode}")

    # Vérifier si le produit existe déjà dans la base locale
    try:
        product = Product.objects.get(barcode=barcode)
        return JsonResponse({
            'name': product.name,
            'category': product.category,
            'brand': product.brand,
            'image_url': product.image_url,
            'recycling_type': product.recycling_type  # Inclure le type de recyclage
        })
    except Product.DoesNotExist:
        # Le produit n'est pas trouvé en local, passer à l'appel de l'API
        pass

    # Appeler l'API Barcode Lookup
    api_url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&key={API_KEY}"
    response = requests.get(api_url)

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        data = response.json()
        # Vérifiez si le produit est disponible dans les résultats de l'API
        if data.get('products'):
            product_data = data['products'][0]
            recycling_type = map_category_to_recycling_type(product_data.get("category", ""))

            # Créez et sauvegardez le produit dans la base locale
            product = Product.objects.create(
                barcode=barcode,
                name=product_data.get("product_name", "Nom indisponible"),
                category=product_data.get("category", "Catégorie indisponible"),
                brand=product_data.get("brand", "Marque indisponible"),
                image_url=product_data.get("images", [""])[0],
                recycling_type=recycling_type  # Nouveau champ
            )
            return JsonResponse({
                'name': product.name,
                'category': product.category,
                'brand': product.brand,
                'image_url': product.image_url,
                'recycling_type': product.recycling_type  # Inclure dans la réponse
            })
        else:
            return JsonResponse({'error': 'Produit non trouvé dans l’API'}, status=404)
    else:
        # Gérez les erreurs d'appel à l'API
        return JsonResponse({'error': f"Erreur lors de l’appel à l’API : {response.status_code}"}, status=500)
