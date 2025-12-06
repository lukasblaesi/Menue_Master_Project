# shopping.py
# -------------------------------------------------------------
# Generiert die Einkaufsliste für den Wochenplan.
# - Unterstützt mehrere Rezepte pro Tag (Listen) und alte Strings.
# - Einfache Einheiten-Normalisierung beim Summieren.
# - Ausgabe in der Konsole und Export nach data/einkaufsliste.txt
# -------------------------------------------------------------
DAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

def generate_shopping_list(weekplan, recipes):
    """Sammelt, zeigt an, speichert."""
    
    totals = _collect_recipes(weekplan, recipes)
    
    _print_totals(totals)
    _save_totals(totals, "data/einkaufsliste.txt")
    print("Einkaufsliste gespeichert: data/einkaufsliste.txt")


# ------------------------------- Sammeln -------------------------------
#Prüfen

g = 0.0
ml = 0.0
el = 0
stk = 0

def _collect_recipes(weekplan, recipes):
    recipes_list = []
    for entry in DAYS:
        val = weekplan[entry]
        if val:
            #print("".join(val))
            recipes_list.append(val)
    for index in range(0, len(recipes_list), 1):
        print(recipes_list[index])
        print()
    return recipes_list
            




# --------------------------- Ausgabe & Speichern ---------------------------

def _print_totals(totals):
    """Schreibt die Einkaufsliste schön formatiert in die Konsole."""
    print("\n--- Einkaufsliste ---")
    print(f"{'Zutat':20} Menge")
    print("-" * 30)

    for (name, unit), amount in totals.items():
        print(f"{name:20} {amount:g} {unit}")


def _save_totals(totals, path):
    """Speichert die Einkaufsliste als Textdatei."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{'Zutat':20} Menge\n")
        f.write("-" * 30 + "\n")
        for (name, unit), amount in totals.items():
            f.write(f"{name:20} {amount:g} {unit}\n")