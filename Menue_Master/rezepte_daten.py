# rezepte_daten.py
"""Lädt Rezepte aus einer Textdatei im Format: Rezept;Zutat;Menge;Einheit."""

def rezepte_aus_datei_laden(dateiname):
    """
    Liest Rezepte aus einer Textdatei ein und baut eine Rezeptliste auf.

    Validierung (minimal):
    - Zeile hat genau 4 Teile (getrennt durch ';')
    - Menge ist numerisch (float)
    """
    rezepte_liste = []

    try:
        datei = open(dateiname, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Fehler: Datei '" + dateiname + "' wurde nicht gefunden.")
        return []
    except OSError:
        print("Fehler: Datei '" + dateiname + "' konnte nicht geöffnet werden.")
        return []

    for zeile in datei:
        zeile = zeile.strip()

        if zeile == "":
            continue

        teile = zeile.split(";")

        if len(teile) != 4:
            print("Zeile übersprungen (falsches Format): " + zeile)
            continue

        rezeptname = teile[0].strip()
        zutatname = teile[1].strip()
        menge_text = teile[2].strip()
        einheit = teile[3].strip()

        try:
            menge = float(menge_text.replace(",", "."))
        except ValueError:
            print("Ungültige Menge, Zeile übersprungen: " + zeile)
            continue

        rezept_gefunden = None
        for rezept in rezepte_liste:
            if rezept["name"] == rezeptname:
                rezept_gefunden = rezept
                break

        if rezept_gefunden is None:
            rezept_gefunden = {
                "name": rezeptname,
                "zutaten": []
            }
            rezepte_liste.append(rezept_gefunden)

        rezept_gefunden["zutaten"].append({
            "name": zutatname,
            "menge": menge,
            "einheit": einheit
        })

    datei.close()
    return rezepte_liste


rezepte_liste = rezepte_aus_datei_laden("daten/rezepte.txt")


wochentage = [
    "Montag", "Dienstag", "Mittwoch",
    "Donnerstag", "Freitag", "Samstag", "Sonntag"
]
