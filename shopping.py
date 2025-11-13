# shopping.py
# -------------------------------------------------------------
# Generiert die Einkaufsliste für den Wochenplan.
# - Unterstützt mehrere Rezepte pro Tag (Listen) und alte Strings.
# - Einfache Einheiten-Normalisierung beim Summieren.
# - Ausgabe in der Konsole und Export nach data/einkaufsliste.txt
# -------------------------------------------------------------

def generate_shopping_list(recipes, weekplan):
    """Kurze Orchestrierung: prüft, sammelt, zeigt an, speichert."""
    if not weekplan:
        print("Kein Wochenplan vorhanden.")
        return

    totals = _collect_totals(recipes, weekplan)
    if not totals:
        print("Keine Zutaten gefunden.")
        return

    _print_totals(totals)
    _save_totals(totals, "data/einkaufsliste.txt")
    print("Einkaufsliste gespeichert: data/einkaufsliste.txt")


# ------------------------------- Sammeln -------------------------------

def _collect_totals(recipes, weekplan):
    """Erzeugt die Summen-Matrix: {(Zutat, Einheit): Menge}."""
    totals = {}
    for _, day_value in weekplan.items():
        for recipe_name in _iter_recipe_names_for_day(day_value):
            recipe = _find_recipe(recipes, recipe_name)
            if recipe is None:
                continue
            for ing in recipe.get("ingredients", []):
                _add_to_totals(totals, ing)
    return totals


def _iter_recipe_names_for_day(value):
    """Gibt eine Liste von Rezeptnamen zurück (kompatibel mit String oder Liste)."""
    if value in (None, "-", []):
        return []
    if isinstance(value, list):
        return value
    return [value]


def _find_recipe(recipes, name):
    """Sucht Rezept nach Name, None wenn nicht gefunden."""
    for r in recipes:
        if r.get("name") == name:
            return r
    return None


def _add_to_totals(totals, ingredient):
    """Fügt eine Zutat in die Totals ein (mit kleiner Normalisierung)."""
    name = str(ingredient.get("name", "")).title()
    unit = _norm_unit(ingredient.get("unit", ""))
    try:
        amount = float(ingredient.get("amount", 0))
    except (TypeError, ValueError):
        amount = 0.0
    key = (name, unit)
    totals[key] = totals.get(key, 0.0) + amount


def _norm_unit(u):
    """Kleine Normalisierung für die Aggregation."""
    u = str(u).strip().lower()
    if u in ("el", "tl"):
        return u.upper()  # EL, TL groß
    mapping = {
        "gramm": "g", "g": "g",
        "kg": "kg",
        "ml": "ml",
        "l": "l", "lt": "l",
        "stk": "stk", "stück": "stk", "stueck": "stk",
    }
    return mapping.get(u, u)


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