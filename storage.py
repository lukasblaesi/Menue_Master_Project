# storage.py
# -------------------------------------------------------------
# Zuständig für das Laden und Speichern der Daten in JSON-Dateien.
# Dateien liegen im Ordner "data/".
# -------------------------------------------------------------

import json
import os

DATA_FOLDER = "data"
FILE_RECIPES = os.path.join(DATA_FOLDER, "recipes.json")
FILE_WEEKPLAN = os.path.join(DATA_FOLDER, "weekplan.json")


def load_data():
    """Lädt Rezepte und Wochenplan. Wenn Dateien nicht existieren, werden leere Daten zurückgegeben."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    recipes = _load_or_empty(FILE_RECIPES, [])
    weekplan = _load_or_empty(FILE_WEEKPLAN, {})

    return recipes, weekplan


def save_data(recipes, weekplan):
    """Speichert die Daten zurück in JSON-Dateien."""
    _save(FILE_RECIPES, recipes)
    _save(FILE_WEEKPLAN, weekplan)


def _load_or_empty(path, default_value):
    """Hilfsfunktion zum Laden von JSON. Fehler -> default_value."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default_value
    except json.JSONDecodeError:
        print(f"Datei beschädigt: {path}. Es wird ein leeres Objekt geladen.")
        return default_value


def _save(path, data):
    """Schreibt JSON zurück auf die Festplatte."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
