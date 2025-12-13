# Projekt_Gruppe3_MenuMaster – Rezept- und Wochenplanungsprogramm (Konsole)
 
Dieses Projekt wird im Rahmen des Moduls **Grundlagen Programmieren** erstellt.
Ziel ist es, eine **Konsolenanwendung** zu entwickeln, mit der Anwender ihre Rezepte verwalten und daraus eine Wochenplanung inklusive Einkaufsliste erstellen können.
 
---
 
## Analyse
 
### **Problem**
 
In vielen Haushalten wird die Wochenplanung für Mahlzeiten manuell geführt, Rezepte liegen auf Papier oder sind über verschiedene Quellen verteilt. Dadurch fehlt Übersicht über benötigte Zutaten und Mengen, was oft zu Mehrfachkäufen oder fehlenden Zutaten führt.
 
Dieses Programm soll den Prozess **digitalisieren, vereinfachen und automatisieren**.
 
---
 
### **Szenario**
 
Ein Anwender möchte seine Rezepte an einem zentralen Ort verwalten.
Die Anwendung ermöglicht es ausserdem, die Rezepte auf Wochentage zu verteilen.
Aus diesen Daten wird automatisch eine Einkaufsliste erstellt, die alle benötigten Zutaten zusammenfasst.
Das Ganze läuft vollständig über die **Kommandozeile (Konsole)**, ohne grafische Oberfläche.
 
---
 
### **User Stories**
 

1. Als Anwender möchte ich, dass meine Rezepte in einer Liste gespeichert werden, die ich jederzeit wieder aufrufen kann.
2. Als Anwender möchte ich meine Rezepte den Wochentagen zuordnen können.
3. Als Anwender möchte ich meine Wochenplanung jederzeit abrufen können.
4. Als Anwender möchte ich nur einen Wochenplan erfassen können. Wenn ich einen neuen Wochenplan erstelle, soll der bestehende Wochenplan ersetzt werden.
5. Als Anwender möchte ich, dass ich bei der Wochenplanung nur aus meinen erfassten Rezepten auswählen kann.
6. Als Anwender möchte ich einen zufälligen Wochenplan erstellen lassen können mit meinen erfassten Rezepten.
7. Als Anwender möchte ich eine wöchentliche Einkaufsliste generieren können, die die Mengen aller für die Woche geplanten Rezepte zusammenfasst.
8. Als Anwender möchte ich das Programm in der Konsole bedienen können, ohne grafische Oberfläche, damit alles einfach bleibt.
 
---
 
### **Use Cases**
 
* Rezeptliste anzeigen
* Wochenplan erstellen (manuell oder zufällig)
* Wochenplan anzeigen
* Einkaufsliste generieren und anzeigen
* Daten speichern und laden
 
---
 
## Projektanforderungen
 
Das Projekt erfüllt die drei Pflichtanforderungen der Aufgabenstellung:
 
1. **Interaktive Anwendung (Konsoleneingaben)**
2. **Datenvalidierung (Eingabeprüfung)**
3. **Dateiverarbeitung (Lesen und Schreiben)**
 
---
 
### 1. Interaktive Anwendung
 
Das Programm läuft vollständig über die **Konsole**.
Der Anwender kann über ein Menü zwischen verschiedenen Funktionen wählen, z.B.:
 
* Rezept anzeigen
* Wochenplan anzeigen oder neu generieren
* Einkaufsliste ausgeben
 
Alle Eingaben erfolgen per Tastatur, die Ausgaben werden übersichtlich im Terminal dargestellt.
 
---
 
### 2. Datenvalidierung
 
Bei der Dateneingabe wird auf **korrekte, vollständige und sinnvolle Eingaben** geachtet.
Beispiele:
 

* Mengenangaben müssen **numerisch** und **grösser als 0** sein.
* Zutaten dürfen **nicht doppelt** innerhalb eines Rezepts vorkommen.
* Beim Auswählen eines Rezepts für den Wochenplan wird geprüft, ob das Rezept **existiert**.
* Das Programm reagiert auf ungültige Eingaben mit **klaren Fehlermeldungen** und fordert eine erneute Eingabe an.
 
---
 
### 3. Dateiverarbeitung
 
Das Programm speichert alle relevanten Daten in **Txt-Dateien** (strukturierte Textformate).
 
#### **Input (Laden beim Start):**
 
* **Rezepte:** Enthält Name, Zutatenliste, Mengen, Portionen
* **Wochenplan:** Zuordnung von Rezepten zu den Wochentagen
 
#### **Output (Speichern oder Ausgabe im Programm):**
 
* **Einkaufsliste:** Automatisch generiert aus allen Rezepten des Wochenplans
 
  * Zutaten werden **zusammengefasst**, wenn sie mehrfach vorkommen
  * Ausgabe sowohl **in der Konsole** als auch optional **in einer Textdatei** (`einkaufsliste.txt`)
 
Beim Start der Anwendung werden vorhandene Dateien automatisch geladen.
Beim Beenden werden alle Änderungen automatisch gespeichert, um Datenverlust zu vermeiden.
 
---
 
## Umsetzung (Implementation)
 
### **Technologie**
 
* Programmiersprache: **Python 3.11.14**
* Entwicklungsumgebung: **GitHub Codespaces / Visual Studio Code**
* Formatierung: **PEP8-konform**
* Externe Bibliotheken: Keine
 
---
 
### **Projektstruktur**
 
---

* main.py: Beinhaltet das Hauptmenü/Programmlogik mit der Übersicht der Unterprogramme des Menü Master Programms.
* anzeigen.py: Beinhaltet sämtliche Funktionen, welche Ausgaben aus der Konsole darstellen, wie Konsolenmenü 1-5 und 0, sowie Anzeigen/Formatierung der Rezepte und Wochenpläne.
* rezepte_daten.py: Rezepte aus der Datei "rezepte.txt" laden.
* wochenplan_funktionen.py: Beinhaltet die Funktionen um einen manuellen und zufälligen Wochenplan mit zugeordneten Rezepten zu erstellen. Ebenfalls ist die Funktion zur Ausgabe und Generierung der Einkaufsliste enthalten.

---
 
### **Starten der Anwendung**
 
---

1. Die kompette Datenablage "Menue_Master" herunterladen und als Projekt als main folder hinterlegen.
2. In der Python Konsole mit "cd" (Change Directory) in den main folder "Menue_Master" navigieren.
3. Das "main.py" starten.

---
 
### **Verwendete Bibliotheken**
 
---
 
* Keine ausserhalb der klassichen Pyhton Bibliothek.
 
---
 
 
## Team & Beiträge
 
| Name      | Beitrag / Verantwortungsbereich                |
| --------- | ---------------------------------------------- |
| Joel N. | Konsolenanzeige / Darstellung Konsole                              |
| Joel R. | Auslesen und Verwaltung der Rezepte                 |
| Lukas B.   | Abfrage Wochenplan mit vorhandenen Menus (Rezepten) / Export Einkaufsliste |
 
---
 
## Zusammenarbeit
 
* Das Projekt wurde im Team im Rahmen der Programmiergrundlagen entwickelt.
* Jeder Studierende war für einen Teilbereich verantwortlich.
* Regelmässige Commits und Code Reviews dienten der **Versionskontrolle** und **Qualitätssicherung**.
* Gemeinsame Tests und Fehlersuche sorgten für eine stabile Endversion.
 
---
 
