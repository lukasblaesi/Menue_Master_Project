# recipes.py
# -------------------------------------------------------------
# Rezepte anzeigen
# -------------------------------------------------------------

def list_recipes(recipes):
    """Namen + Portionen anzeigen (Reihenfolge = aktuelle Listenreihenfolge)."""
    for i, r in enumerate(recipes):
        print(f"{i+1}. {r['name']} (Portionen: {r['portions']})")

    return recipes
