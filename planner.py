# planner.py
# -------------------------------------------------------------
# Wochenplan erstellen (manuell oder zufällig)
# - Pro Tag können mehrere Rezepte erfasst werden.
# - Eingabe: Nummern durch Komma getrennt (z. B. "1,3,5"), Enter = keins.
# - Anzeige: "Name1, Name2"
# -------------------------------------------------------------

DAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

def show_weekplan(weekplan):
    """Zeigt den Wochenplan. Werte können Strings (alt) oder Listen (neu) sein."""
    if not weekplan:
        print("Noch kein Wochenplan vorhanden.")
        return

    print("\n--- Wochenplan ---")
    for day in DAYS:
        val = weekplan.get(day, []) #Nimmt Liste aus dem Tag, wenn nichts drin = Leer
        
        if not val: 
            print(f"{day:11}:")
        else:
            print(f"{day:11}: {', '.join(val)}") #.join eventeull anpassen später / join = Mehrere Strings zu einem

def create_manual_weekplan(recipes):
    """Erstellt den Wochenplan per Eingabe im Terminal."""
    if not recipes:
        print("Keine Rezepte vorhanden.")
        return {}

    # Rezeptnamen-Liste ohne List-Comprehension
    names = []
    for recipe in recipes:
        names.append(recipe["name"])

    _print_recipe_list(names)
    print("\nEingabe pro Tag: mehrere Nummern durch Komma (z. B. 1,3,5). Enter = kein Gericht.")

    new_plan = {}

    for day in DAYS:
        selection = _ask_day_selection(day, names)  # gibt Liste von Namen zurück (oder leere Liste)
        new_plan[day] = selection   # kein "-" mehr, nur [] wenn leer

    print("Wochenplan gespeichert.")
    return new_plan


def create_random_weekplan(recipes):
    """Zufälliger Wochenplan: 1 Rezept pro Tag."""
    import random

    if not recipes:
        print("Keine Rezepte vorhanden.")
        return {}

    names = []
    for recipe in recipes:
        names.append(recipe["name"])

    new_plan = {}
    for day in DAYS:
        zufalls_rezept = random.choice(names)
        new_plan[day] = [zufalls_rezept]   # als Liste speichern

    print("Zufälliger Wochenplan erstellt.")
    return new_plan


# ----------------------------- Helfer -----------------------------

def _print_recipe_list(names):
    print("\nVerfügbare Rezepte:")
    for i, name in enumerate(names):
        print(f"{i+1}. {name}")

"""
Sinnvoller so?

def _print_recipe_list(names):
    print("\nVerfügbare Rezepte:")
    index = 1
    for name in names:
        print(f"{index}. {name}")
        index += 1
"""

def _ask_day_selection(day, names):
    """Fragt wiederholt, bis eine gültige Eingabe oder Enter erfolgt.
       Rückgabe: Liste von Rezeptnamen oder leere Liste (für '-')."""
    while True:
        """
        raw = input(f"{day}: ").strip()
        if raw == "":
            return []
        parts = [p.strip() for p in raw.split(",") if p.strip() != ""]
        """
        raw = input(day + ": ").strip()

        if raw == "": #Wenn Enter = Leere Liste
            return []

        parts = []

        splitted = raw.split(",") #Abstand zwischen , wird eingefügt

        for p in splitted: #Nummern werden nochmals bearbeitet
            p = p.strip()
            if p != "":
                parts.append(p)
        
        if not _all_indices_valid(parts, len(names)):
            print("Ungültige Nummer(n). Bitte gültige Nummern im Bereich angeben oder Enter für '-'.")
            continue
        return _indices_to_names(parts, names)


def _all_indices_valid(parts, max_len):
    """Prüft, ob alle Teile Ganzzahlen im erlaubten Bereich sind."""
    for p in parts:
        if not (p.isdigit() and 1 <= int(p) <= max_len): #String darf nur Ziffern haben (p.isdigit)
            return False
    return True


def _indices_to_names(parts, names):
    """Wandelt Index-Strings in Rezeptnamen um und entfernt Duplikate (Reihenfolge bleibt)."""
    selected = []
    for p in parts:
        name = names[int(p) - 1] #Listen-Index beginnt immer bei 0
        if name not in selected: #Duplikatsprüfung
            selected.append(name)
    return selected

