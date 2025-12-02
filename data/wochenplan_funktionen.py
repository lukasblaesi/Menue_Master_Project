# wochenplan_funktionen.py
# Enthält die Funktionen für:
# - Rezeptauswahl
# - Wochenplan (manuell / zufällig)
# - Einkaufsliste erstellen und speichern

import random
from rezepte_daten import rezepte_liste, wochentage

def rezept_liste_anzeigen_kurz():
    # Zeigt alle Rezepte nur mit Nummer und Name an.
    print()
    print("Verfügbare Rezepte:")
    nummer = 1

    for rezept in rezepte_liste:
        print(str(nummer) + ") " + rezept["name"])
        nummer += 1

    print()

def rezept_auswahl():
    """
    Fragt den Benutzer nach einer Rezeptnummer.
    Validierungen:
    - Eingabe ist Zahl?
    - Zahl innerhalb der vorhandenen Rezepte?
    """
    while True:
        eingabe = input("Bitte Rezeptnummer eingeben (oder Enter für kein Rezept): ").strip()

        # Kein Rezept für diesen Tag
        if eingabe == "":
            return None

        # Prüfen ob Zahl
        if eingabe.isdigit():
            nummer = int(eingabe)

            # Bereich prüfen
            if 1 <= nummer <= len(rezepte_liste):
                return nummer - 1

        # Falls ungültig
        print("Ungültige Eingabe. Bitte nochmal versuchen.")

def wochenplan_manuell_erstellen(wochenplan):
    # Benutzer wählt für jeden Tag ein Rezept aus.
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
    # Wählt für jeden Tag zufällig ein Rezept aus.
    print()
    print("====== Zufälligen Wochenplan erstellen ======")

    for i in range(len(wochentage)):
        wochenplan[i] = random.randint(0, len(rezepte_liste) - 1)

    print("Ein zufälliger Wochenplan wurde erstellt.\n")

def einkaufsliste_erstellen(wochenplan):
    """
    Erstellt eine Einkaufsliste.
    Schlüssel = (Zutatname, Einheit)
    Wert     = gesamte Menge
    """
    einkaufsliste = {}

    # Durch die geplanten Rezepte gehen
    for rezept_index in wochenplan:
        if rezept_index is not None:
            rezept = rezepte_liste[rezept_index]

            # Alle Zutaten dieses Rezepts hinzufügen
            for z in rezept["zutaten"]:
                schluessel = (z["name"], z["einheit"])

                if schluessel in einkaufsliste:
                    einkaufsliste[schluessel] += z["menge"]
                else:
                    einkaufsliste[schluessel] = z["menge"]

    return einkaufsliste

def einkaufsliste_anzeigen(wochenplan):
    # Einkaufsliste anzeigen und zusätzlich speichern.
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

    # In Unterordner speichern
    try:
        datei = open("daten/einkaufsliste.txt", "w", encoding="utf-8")

        # Titel schreiben
        datei.write("Einkaufsliste\n")
        datei.write("=============\n\n")

        # Zeilen schreiben
        for text in zeilen:
            datei.write(text + "\n")

        datei.close()
        print("Einkaufsliste wurde in 'daten/einkaufsliste.txt' gespeichert.\n")

    except:
        print("Einkaufsliste konnte nicht gespeichert werden.\n")
