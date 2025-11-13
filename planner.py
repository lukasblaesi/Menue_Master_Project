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
        val = weekplan.get(day, "-")
        if val == "-" or val == [] or val is None:
            print(f"{day:11}: -")
        elif isinstance(val, list):
            print(f"{day:11}: {', '.join(val)}")
        else:
            print(f"{day:11}: {val}")


def create_manual_weekplan(recipes):
    """Manuelle Erfassung mit kurzer, gut lesbarer Logik."""
    if not recipes:
        print("Keine Rezepte vorhanden.")
        return {}

    names = [r["name"] for r in recipes]
    _print_recipe_list(names)
    print("\nEingabe pro Tag: mehrere Nummern durch Komma (z. B. 1,3,5). Enter = kein Gericht.")

    new_plan = {}
    for day in DAYS:
        selection = _ask_day_selection(day, names)
        new_plan[day] = selection if selection else "-"
    print("Wochenplan gespeichert.")
    return new_plan


def create_random_weekplan(recipes):
    """Zufälliger Wochenplan: aus Einfachheit 1 Rezept pro Tag (als Liste)."""
    import random
    names = [r["name"] for r in recipes]
    new_plan = {day: [random.choice(names)] for day in DAYS}
    print("Zufälliger Wochenplan erstellt.")
    return new_plan


# ----------------------------- Helfer -----------------------------

def _print_recipe_list(names):
    print("\nVerfügbare Rezepte:")
    for i, name in enumerate(names):
        print(f"{i+1}. {name}")


def _ask_day_selection(day, names):
    """Fragt wiederholt, bis eine gültige Eingabe oder Enter erfolgt.
       Rückgabe: Liste von Rezeptnamen oder leere Liste (für '-')."""
    while True:
        raw = input(f"{day}: ").strip()
        if raw == "":
            return []
        parts = [p.strip() for p in raw.split(",") if p.strip() != ""]
        if not _all_indices_valid(parts, len(names)):
            print("Ungültige Nummer(n). Bitte gültige Nummern im Bereich angeben oder Enter für '-'.")
            continue
        return _indices_to_names(parts, names)


def _all_indices_valid(parts, max_len):
    """Prüft, ob alle Teile Ganzzahlen im erlaubten Bereich sind."""
    for p in parts:
        if not (p.isdigit() and 1 <= int(p) <= max_len):
            return False
    return True


def _indices_to_names(parts, names):
    """Wandelt Index-Strings in Rezeptnamen um und entfernt Duplikate (Reihenfolge bleibt)."""
    selected = []
    for p in parts:
        name = names[int(p) - 1]
        if name not in selected:
            selected.append(name)
    return selected