def map_category_to_recycling_type(category):
    category = category.lower()

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
        "fruit peels", "vegetable peels", "food scraps", "coffee grounds", "tea bags",
        "eggshells", "stale bread", "spoiled fruits", "spoiled vegetables", "wilted flowers",
        "paper tissues", "paper towels", "dead leaves", "grass clippings", "small branches",
        "wood sawdust", "straw", "hay", "cooled wood ashes"
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
        "batteries", "electronic devices", "energy-saving bulbs", "leds", "expired medications",
        "chemical products", "paints", "solvents", "motor oil", "ink cartridges", "x-rays",
        "fluorescent tubes", "mercury thermometers", "pesticides", "insecticides", "car batteries",
        "electrical equipment", "mobile phones", "computers", "tablets", "small appliances",
        "cds", "dvds", "printer toners", "hazardous diy products", "electronic toys", "power banks",
        "cables", "chargers"
    ]):
        return "Special Waste"

    # Default
    return "Autre"
