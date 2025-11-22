# storage.py
# -------------------------------------------------------------
# Zuständig für das Laden und Speichern der Daten in JSON-Dateien.
# Dateien liegen im Ordner "data/".
# -------------------------------------------------------------

import json
import os

DATA_FOLDER = "data"
FILE_RECIPES = "data/recipes.json"
FILE_WEEKPLAN = "data/weekplan.json"


def load_data():
    """Lädt Rezepte und Wochenplan. Wenn Dateien nicht existieren, werden leere Daten zurückgegeben."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    recipes = _load_or_empty(FILE_RECIPES)
    weekplan = _load_or_empty(FILE_WEEKPLAN)

    return recipes, weekplan


def save_data(weekplan):
    """Prüft ob Ordner existiert, ansonsten wird einer erstellt."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    """Speichert den Wochenplan."""
    with open(FILE_WEEKPLAN, "w", encoding="utf-8") as f:
        json.dump(weekplan, f, indent=2, ensure_ascii=False)



def _load_or_empty(path):
    """Prüft ob Datei existiert."""
    try:
        with open(path, "r")as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Folgendes file konnte nicht gefunden werden: {path}")