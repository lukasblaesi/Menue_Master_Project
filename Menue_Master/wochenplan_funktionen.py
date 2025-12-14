# wochenplan_funktionen.py
"""Logik für Wochenplan, Rezeptauswahl und Einkaufsliste (Konsole)."""

import random

from rezepte_daten import rezepte_liste
from rezepte_daten import wochentage


def rezept_liste_anzeigen_kurz():
    """Zeigt alle Rezepte nummeriert an, damit man sie auswählen kann."""
    print()
    print("Verfügbare Rezepte:")
    nummer = 1

    for rezept in rezepte_liste:
        print(str(nummer) + ") " + rezept["name"])
        nummer += 1

    print()


def rezept_auswahl():
    """
    Fragt eine Rezeptnummer ab und validiert die Eingabe.

    Rückgabe:
    - Index (0-basiert) eines Rezepts oder
    - None, wenn Enter gedrückt wurde
    """
    while True:
        eingabe = input(
            "Bitte Rezeptnummer eingeben (oder Enter für kein Rezept): "
        ).strip()

        if eingabe == "":
            return None

        if eingabe.isdigit():
            nummer = int(eingabe)

            if 1 <= nummer <= len(rezepte_liste):
                return nummer - 1

        print("Ungültige Eingabe. Bitte nochmal versuchen.")


def wochenplan_manuell_erstellen(wochenplan):
    """Ersetzt den Wochenplan durch neue Werte (manuelle Eingabe)."""
    print()
    print("====== Wochenplan manuell erstellen ======")

    for i in range(len(wochentage)):
        print()
        print("--- " + wochentage[i] + " ---")

        rezept_liste_anzeigen_kurz()
        rezept_index = rezept_auswahl()
        wochenplan[i] = rezept_index

        if rezept_index is None:
            print("Kein Rezept eingetragen.")
        else:
            print("Rezept eingetragen: " + rezepte_liste[rezept_index]["name"])

    print("\nDer neue Wochenplan wurde erstellt.\n")


def wochenplan_zufaellig_erstellen(wochenplan):
    """Ersetzt den Wochenplan durch zufällige Rezepte aus der Rezeptliste."""
    print()
    print("====== Zufälligen Wochenplan erstellen ======")

    for i in range(len(wochentage)):
        wochenplan[i] = random.randint(0, len(rezepte_liste) - 1)

    print("Ein zufälliger Wochenplan wurde erstellt.\n")


def einkaufsliste_erstellen(wochenplan):
    """
    Erstellt eine Einkaufsliste mit zusammengefassten Mengen.

    Schlüssel: (Zutatname, Einheit)
    Wert: Gesamtmenge (Summe über die Woche)
    """
    einkaufsliste = {}

    for rezept_index in wochenplan:
        if rezept_index is not None:
            rezept = rezepte_liste[rezept_index]

            for z in rezept["zutaten"]:
                schluessel = (z["name"], z["einheit"])

                if schluessel in einkaufsliste:
                    einkaufsliste[schluessel] += z["menge"]
                else:
                    einkaufsliste[schluessel] = z["menge"]

    return einkaufsliste


def einkaufsliste_anzeigen(wochenplan):
    """Gibt die Einkaufsliste aus und speichert sie als Textdatei."""
    print()
    print("====== Einkaufsliste ======")

    einkaufsliste = einkaufsliste_erstellen(wochenplan)

    if len(einkaufsliste) == 0:
        print("Es sind keine Zutaten vorhanden. Wochenplan leer?")
        print()
        return

    zeilen = []

    for (name, einheit), menge in einkaufsliste.items():
        text = "- " + str(menge) + " " + einheit + " " + name
        print(text)
        zeilen.append(text)

    print()

    try:
        datei = open("daten/einkaufsliste.txt", "w", encoding="utf-8")

        datei.write("Einkaufsliste\n")
        datei.write("=============\n\n")

        for text in zeilen:
            datei.write(text + "\n")

        datei.close()
        print("Einkaufsliste wurde in 'daten/einkaufsliste.txt' gespeichert.\n")

    except OSError:
        print("Einkaufsliste konnte nicht gespeichert werden.\n")
