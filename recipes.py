# recipes.py
# -------------------------------------------------------------
# Rezepte anzeigen
# -------------------------------------------------------------
"""
def menu_recipes(recipes):
    Menü zur Verwaltung von Rezepten.
    while True:
        print("\n--- Rezepte ---")
        print("1) Rezeptliste anzeigen")
        print("0) Zurück")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            list_recipes(recipes); input("\nWeiter mit Enter...")
        elif choice == "0":
            return recipes
        else:
            print("Ungültige Auswahl.")
"""


def list_recipes(recipes):
    """Namen + Portionen anzeigen (Reihenfolge = aktuelle Listenreihenfolge)."""
    for i, r in enumerate(recipes):
        print(f"{i+1}. {r['name']} (Portionen: {r['portions']})")
