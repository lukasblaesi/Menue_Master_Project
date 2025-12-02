# rezepte_daten.py
# Dieses Modul lädt alle Rezepte aus einer Textdatei.
# Format pro Zeile: Rezeptname;Zutatname;Menge;Einheit
# Die Datei liegt im Unterordner "daten/rezepte.txt".

def rezepte_aus_datei_laden(dateiname):
    """
    Liest Rezepte aus einer Textdatei.
    Baut eine einfache Liste von Rezepten auf.
    Validierung: Format und numerische Menge.
    """

    rezepte_liste = []

    # Datei öffnen
    try:
        datei = open(dateiname, "r", encoding="utf-8")
    except:
        print("Fehler: Datei '" + dateiname + "' wurde nicht gefunden.")
        return []

    # Datei Zeile für Zeile lesen
    for zeile in datei:
        zeile = zeile.strip()

        # Leere Zeilen ignorieren
        if zeile == "":
            continue

        teile = zeile.split(";")

        # Format prüfen: genau 4 Teile
        if len(teile) != 4:
            print("Zeile übersprungen (falsches Format): " + zeile)
            continue

        rezeptname = teile[0].strip()
        zutatname = teile[1].strip()
        menge_text = teile[2].strip()
        einheit = teile[3].strip()

        # Menge in Zahl umwandeln
        try:
            menge = float(menge_text.replace(",", "."))
        except ValueError:
            print("Ungültige Menge, Zeile übersprungen: " + zeile)
            continue

        # Rezept in der Liste suchen
        rezept_gefunden = None
        for rezept in rezepte_liste:
            if rezept["name"] == rezeptname:
                rezept_gefunden = rezept
                break

        # Wenn nicht gefunden: neues Rezept in die Liste einfügen
        if rezept_gefunden is None:
            rezept_gefunden = {
                "name": rezeptname,
                "zutaten": []
            }
            rezepte_liste.append(rezept_gefunden)

        # Zutat einfach hinzufügen (keine Duplikat-Prüfung)
        rezept_gefunden["zutaten"].append({
            "name": zutatname,
            "menge": menge,
            "einheit": einheit
        })

    datei.close()
    return rezepte_liste


# Rezepte aus Datei laden (Unterordner daten/)
rezepte_liste = rezepte_aus_datei_laden("daten/rezepte.txt")

# Liste der Wochentage
wochentage = [
    "Montag", "Dienstag", "Mittwoch",
    "Donnerstag", "Freitag", "Samstag", "Sonntag"
]
