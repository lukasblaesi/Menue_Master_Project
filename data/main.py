# main.py
# Dies ist das Hauptprogramm.
# Hier läuft die Menü-Schleife und steuert den Ablauf des Programms.

from anzeigen import menue_anzeigen, rezepte_anzeigen, wochenplan_anzeigen
from wochenplan_funktionen import (
    wochenplan_manuell_erstellen,
    wochenplan_zufaellig_erstellen,
    einkaufsliste_anzeigen,
)

def hauptprogramm():
    # Wochenplan: Für jeden der 7 Tage steht hier eine Rezeptnummer (Index) oder None.
    wochenplan = [None, None, None, None, None, None, None]

    while True:
        # Menü anzeigen
        menue_anzeigen()
        # Eingabe lesen
        auswahl = input("Bitte Zahl eingeben: ").strip()
        # Auswertung der Eingabe
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
            # Wenn eine falsche Zahl eingegeben wird
            print("Ungültige Eingabe. Bitte nochmal versuchen.")

# Programmstart
if __name__ == "__main__":
    hauptprogramm()
