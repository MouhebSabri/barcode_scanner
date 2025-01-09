def map_category_to_recycling_type(category):
    category = category.lower()
    unknown_categories_file = "unknown_categories.txt"  # Fichier pour collecter les catégories inconnues

    # Recyclables
    if any(keyword in category for keyword in [
        "plastic bottles", "plastic containers", "cardboard", "paperboard", "papers",
        "newspapers", "magazines", "flyers", "envelopes", "tin cans", "aluminum cans",
        "food cartons", "beverage cartons", "metal boxes", "recyclable plastic films",
        "recyclable plastic bags", "empty aerosol cans", "aluminum trays", "cardboard packaging",
        "non-plastic coated gift wrap", "clean aluminum foil"
    ]):
        return "Recyclables"

    # Compostable
    elif any(keyword in category for keyword in [
        "tea", "infusions", "coffee grounds", "tea bags", "fruit peels", "vegetable peels",
        "food scraps", "organic", "compostable"
    ]):
        return "Compostable"

    # Glass
    elif any(keyword in category for keyword in [
        "glass bottles", "jars", "perfume bottles", "glass oil bottles", "glass yogurt pots",
        "jam jars", "wine bottles", "spirits bottles", "medicine glass bottles"
    ]):
        return "Glass"

    # General Waste
    elif any(keyword in category for keyword in [
        "soiled packaging", "diapers", "hygiene items", "broken dishes", "broken mirrors",
        "filament light bulbs", "vacuum cleaner bags", "used pens", "chewing gum", "cigarette butts",
        "disposable masks", "disposable gloves", "non-recyclable packaging", "soiled aluminum foil",
        "styrofoam containers", "non-recyclable hard plastic", "broken ceramics",
        "used tissues", "used napkins"
    ]):
        return "General Waste"

    # Special Waste
    elif any(keyword in category for keyword in [
        "battery", "electronics", "motor vehicle", "vehicle parts", "oil", "engine", "tires",
        "brake", "hazardous", "chemical products", "paints", "solvents", "ink cartridges",
        "pesticides", "insecticides", "car batteries", "mobile phones", "computers", "tablets",
        "small appliances", "cds", "dvds", "printer toners", "fluorescent tubes", "mercury thermometers"
    ]):
        return "Special Waste"

    # Enregistrer les catégories inconnues pour analyse future
    with open(unknown_categories_file, "a") as file:
        file.write(f"{category}\n")

    # Par défaut, retourner "Autre"
    return "Autre"
