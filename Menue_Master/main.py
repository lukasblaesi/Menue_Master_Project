# main.py
"""Startpunkt der Konsolenanwendung (Menüführung und Programmablauf)."""

from anzeigen import menue_anzeigen
from anzeigen import rezepte_anzeigen
from anzeigen import wochenplan_anzeigen
from wochenplan_funktionen import einkaufsliste_anzeigen
from wochenplan_funktionen import wochenplan_manuell_erstellen
from wochenplan_funktionen import wochenplan_zufaellig_erstellen


def hauptprogramm():
    """Startet die Menü-Schleife und ruft die gewählten Funktionen auf."""
    wochenplan = [None, None, None, None, None, None, None]

    while True:
        menue_anzeigen()

        auswahl = input("Bitte Zahl eingeben: ").strip()

        if auswahl == "1":
            rezepte_anzeigen()
        elif auswahl == "2":
            wochenplan_anzeigen(wochenplan)
        elif auswahl == "3":
            wochenplan_manuell_erstellen(wochenplan)
        elif auswahl == "4":
            wochenplan_zufaellig_erstellen(wochenplan)
        elif auswahl == "5":
            einkaufsliste_anzeigen(wochenplan)
        elif auswahl == "0":
            print("Programm wird beendet. Tschüss!")
            break
        else:
            print("Ungültige Eingabe. Bitte nochmal versuchen.")


if __name__ == "__main__":
    hauptprogramm()
