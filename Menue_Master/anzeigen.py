# anzeigen.py
"""Ausgabe-Modul: enthält nur Funktionen, die Text in der Konsole anzeigen."""

from rezepte_daten import rezepte_liste
from rezepte_daten import wochentage


def menue_anzeigen():
    """Gibt das Hauptmenü aus (rein zur Benutzerführung)."""
    print()
    print("====== Rezept- und Wochenplaner ======")
    print("1) Rezepte anzeigen")
    print("2) Wochenplan anzeigen")
    print("3) Wochenplan manuell erstellen")
    print("4) Wochenplan zufällig erstellen")
    print("5) Einkaufsliste anzeigen")
    print("0) Programm beenden")
    print()


def rezepte_anzeigen():
    """Zeigt alle geladenen Rezepte inkl. Zutaten an."""
    if len(rezepte_liste) == 0:
        print("Es sind keine Rezepte vorhanden.")
        return

    print()
    print("====== Rezepte ======")

    nummer = 1
    for rezept in rezepte_liste:
        print()
        print(str(nummer) + ") " + rezept["name"])
        print("   Zutaten:")

        for zutat in rezept["zutaten"]:
            menge = zutat["menge"]
            einheit = zutat["einheit"]
            name = zutat["name"]
            print("   - " + str(menge) + " " + einheit + " " + name)

        nummer += 1

    print()


def wochenplan_anzeigen(wochenplan):
    """Zeigt den aktuellen Wochenplan an (Tag -> Rezept oder leer)."""
    print()
    print("====== Aktueller Wochenplan ======")

    for i in range(len(wochentage)):
        tag = wochentage[i]
        rezept_index = wochenplan[i]

        if rezept_index is None:
            text = "(kein Rezept)"
        else:
            text = rezepte_liste[rezept_index]["name"]

        print(tag + ": " + text)

    print()
