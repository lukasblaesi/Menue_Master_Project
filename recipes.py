# recipes.py
# -------------------------------------------------------------
# Rezepte verwalten:
# - Anlegen / Ändern / Löschen / Anzeigen
# - Zutaten-Menü (add / edit / delete)
# - Wochenplan wird beim Umbenennen/Löschen konsistent gehalten
# -------------------------------------------------------------

def menu_recipes(recipes, weekplan):
    """Menü zur Verwaltung von Rezepten."""
    while True:
        print("\n--- Rezepte ---")
        print("1) Rezept anlegen")
        print("2) Rezept ändern")
        print("3) Rezept löschen")
        print("4) Rezeptliste anzeigen")
        print("0) Zurück")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            edit_recipe(recipes, weekplan)
        elif choice == "3":
            delete_recipe(recipes, weekplan)
        elif choice == "4":
            list_recipes(recipes); input("\nWeiter mit Enter...")
        elif choice == "0":
            return recipes
        else:
            print("Ungültige Auswahl.")


# -------------------------------------------------------------
# Rezept anlegen / ändern / löschen
# -------------------------------------------------------------

def add_recipe(recipes):
    """Neues Rezept hinzufügen (kurz, nutzt Helfer)."""
    name = input_recipe_name(recipes)
    portions = input_portions()
    ingredients = input_ingredients()
    recipes.append({"name": name, "portions": portions, "ingredients": ingredients})
    print("Rezept gespeichert.")


def edit_recipe(recipes, weekplan):
    """Rezept auswählen und ändern (kurz, delegiert an Helfer)."""
    idx = _select_recipe_index_or_return(recipes)
    if idx is None:
        return

    recipe = recipes[idx]
    _print_edit_menu(recipe["name"])
    choice = input("Auswahl: ").strip()

    if choice == "1":
        _edit_name(recipes, weekplan, recipe)
    elif choice == "2":
        _edit_portions(recipe)
    elif choice == "3":
        ingredients_menu(recipe)
    else:
        print("Ungültige Auswahl.")


def delete_recipe(recipes, weekplan):
    """Rezept löschen (kurz, delegiert an Helfer)."""
    idx = _select_recipe_index_or_return(recipes)
    if idx is None:
        return

    name = recipes[idx]["name"]
    if ask_yes_no(f"Sicher löschen: {name}? (j/n)") == "n":
        return

    recipes.pop(idx)
    _remove_recipe_from_weekplan(weekplan, name)
    print("Rezept gelöscht und Wochenplan bereinigt.")


# ------------------------- Edit-Helfer ------------------------

def _select_recipe_index_or_return(recipes):
    """Gemeinsame Auswahl-Logik für edit/delete."""
    if not recipes:
        print("Keine Rezepte vorhanden.")
        return None
    list_recipes(recipes)
    return ask_index(len(recipes))


def _print_edit_menu(name):
    print(f"Rezept ändern: {name}")
    print("1) Namen ändern")
    print("2) Portionen ändern")
    print("3) Zutaten bearbeiten")


def _edit_name(recipes, weekplan, recipe):
    """Name ändern und Woche aktualisieren."""
    old = recipe["name"]
    new = input_non_empty("Neuer Name").title()
    if any(r["name"] == new for r in recipes) and new != old:
        print("Name existiert bereits.")
        return
    recipe["name"] = new
    _rename_recipe_in_weekplan(weekplan, old, new)
    print("Name geändert und Wochenplan aktualisiert.")


def _edit_portions(recipe):
    """Portionen setzen."""
    recipe["portions"] = input_portions()
    print("Portionen geändert.")


def _rename_recipe_in_weekplan(weekplan, old_name, new_name):
    """Ersetzt Namens-Vorkommen im Wochenplan (String oder Liste)."""
    for day, val in list(weekplan.items()):
        if val in (None, "-", []):
            continue
        if isinstance(val, list):
            weekplan[day] = [new_name if r == old_name else r for r in val]
            if not weekplan[day]:
                weekplan[day] = "-"
        else:
            if val == old_name:
                weekplan[day] = new_name


def _remove_recipe_from_weekplan(weekplan, name):
    """Entfernt ein Rezept aus dem Wochenplan (String oder Liste)."""
    for day, val in list(weekplan.items()):
        if val in (None, "-", []):
            continue
        if isinstance(val, list):
            weekplan[day] = [r for r in val if r != name]
            if not weekplan[day]:
                weekplan[day] = "-"
        else:
            if val == name:
                weekplan[day] = "-"


# -------------------------------------------------------------
# Zutaten-Menü (klein und klar)
# -------------------------------------------------------------

def ingredients_menu(recipe):
    """Einfaches Untermenü für Zutaten."""
    while True:
        print("\nZutaten:")
        for i, z in enumerate(recipe["ingredients"]):
            print(f"{i+1}. {z['name']} - {z['amount']} {z['unit']}")
        print("1) Zutat hinzufügen")
        print("2) Zutat ändern")
        print("3) Zutat löschen")
        print("0) Fertig")
        choice = input("Auswahl: ").strip()

        if choice == "1":
            add_ingredient(recipe)
        elif choice == "2":
            edit_ingredient(recipe)
        elif choice == "3":
            remove_ingredient(recipe)
        elif choice == "0":
            break
        else:
            print("Ungültige Auswahl.")


def add_ingredient(recipe):
    name = input_non_empty("Zutat").title()
    if any(z["name"] == name for z in recipe["ingredients"]):
        print("Zutat existiert bereits.")
        return
    amount = input_amount()
    unit = validate_unit()
    recipe["ingredients"].append({"name": name, "amount": amount, "unit": unit})


def edit_ingredient(recipe):
    if not recipe["ingredients"]:
        print("Keine Zutaten vorhanden.")
        return
    idx = ask_index(len(recipe["ingredients"]))
    if idx is None:
        return
    z = recipe["ingredients"][idx]
    z["name"] = input_non_empty("Neuer Name").title()
    z["amount"] = input_amount()
    z["unit"] = validate_unit()


def remove_ingredient(recipe):
    if not recipe["ingredients"]:
        print("Keine Zutaten vorhanden.")
        return
    idx = ask_index(len(recipe["ingredients"]))
    if idx is None:
        return
    removed = recipe["ingredients"].pop(idx)
    print(f"Entfernt: {removed['name']}")


# -------------------------------------------------------------
# Eingabe-Hilfen
# -------------------------------------------------------------

def input_recipe_name(recipes):
    """Nicht leer, eindeutig, Title-Case."""
    while True:
        name = input_non_empty("Name").title()
        if any(r["name"] == name for r in recipes):
            print("Rezeptname existiert bereits.")
        else:
            return name


def input_portions():
    """Ganzzahl >= 1."""
    while True:
        raw = input("Portionen (Ganzzahl >= 1): ").strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("Ungültig. Beispiel: 2")


def input_ingredients():
    """Mehrere Zutaten abfragen, bis der Nutzer fertig ist. Nur j/n erlaubt."""
    result = []
    while True:
        if ask_yes_no("Zutat hinzufügen? (j/n)") == "n":
            break
        name = input_non_empty("Zutat").title()
        if any(z["name"] == name for z in result):
            print("Zutat existiert bereits.")
            continue
        amount = input_amount()
        unit = validate_unit()
        result.append({"name": name, "amount": amount, "unit": unit})
    return result


def input_amount():
    """Zahl > 0, Dezimalpunkt oder Komma erlaubt."""
    while True:
        raw = input("Menge (Zahl > 0): ").strip().replace(",", ".")
        try:
            val = float(raw)
            if val > 0:
                return val
            print("Bitte eine Zahl > 0 eingeben.")
        except ValueError:
            print("Ungültige Zahl.")


def input_non_empty(label):
    """Nicht-leere Eingabe anfordern."""
    while True:
        value = input(f"{label}: ").strip()
        if value != "":
            return value
        print("Eingabe darf nicht leer sein.")


def validate_unit():
    """Einheit aus Whitelist, einfache Schreibweise."""
    valid = ["g", "kg", "ml", "l", "stk", "el", "tl"]
    while True:
        unit = input("Einheit (g, kg, ml, l, stk, el, tl): ").strip().lower()
        if unit in valid:
            return unit.upper() if unit in ("el", "tl") else unit
        print("Ungültige Einheit.")


def ask_yes_no(prompt):
    """Fragt strikt j/n ab, alles andere wird erneut gefragt."""
    while True:
        ans = input(f"{prompt} ").strip().lower()
        if ans in ("j", "n"):
            return ans
        print("Bitte mit 'j' oder 'n' antworten.")


def list_recipes(recipes):
    """Namen + Portionen anzeigen (Reihenfolge = aktuelle Listenreihenfolge)."""
    for i, r in enumerate(recipes):
        print(f"{i+1}. {r['name']} (Portionen: {r['portions']})")


def ask_index(max_index):
    """Auswahl per Nummer (1..max_index), Enter = Abbruch."""
    raw = input(f"Nummer wählen (1-{max_index}, Enter = abbrechen): ").strip()
    if raw == "":
        return None
    if raw.isdigit() and 1 <= int(raw) <= max_index:
        return int(raw) - 1
    print("Ungültige Nummer.")
    return None