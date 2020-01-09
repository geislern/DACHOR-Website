# [WIP] DACHOR-darmstadt.de


## Beschreibung

Dieses Django Projekt steckt hinter der Website auf DACHOR-Darmstadt.de und bildet den Webauftritt des DA!CHOR in Darmstadt.

Das Repository enthält ein Django Prpjekt mit einer einzelnen App, die die Website und den internen Bereich bereitstellt.


## Setup

Das Setup entspricht weitgehend allen weiteren Django Projekten.


### Requirements

Um die Anwendung deployen zu können, entweder zur weiteren Entwicklung, oder als Produktivsystem, werden zwei Arten von Abhängigkeiten/Requirements benöigt. System Requirements sind abhängig vom Betriebssystem, und müssen aus entsprechender Quelle im Vorhinein installiert werden.

Python Requirements werden im Laufe des Setups in einer virtuellen Umgebung, und somit für alle Maschinen auf die gleiche Weise installiert. Dieses Projekt verwendet dafür ````pip````.


#### System Requirements

Dieses Projekt verwendet ````Python 3.8```` und ````Django 3.0````.
Um den Instruktionen für Entwicklung und Setup zu folgen wird außerdem ````Virtualenv```` und die entsprechenden Python Dev Tools benötigt.

Um die Anwendung produktiv zu deployen, wird außerdem benötigt:

* C compiler (gcc)
* uwsgi
* uwsgi Python3 Plugin
* falls Apache verwendet wird: das mod proxy uwsgi Plugin


#### Python Requirements

Die Python Requirements inkl. der kompatiblen Versionsnummern, werden in der Datei ````requirements.txt```` verwaltet. Mit ````pip```` werden sie mit dem Befehl ````pip install -r requirements```` installiert.


### Entwicklungs-Setup

* erstelle ein neues Verzeichnis, das in Zukunft die Projektdateien enthalten soll, z.B. ````mkdir DACHOR-website````
* wechsle in das neue Verzeichnis ````cd DACHOR-website````
* klone dieses git ````git clone $URL . ````

**Automatisches Setup**

Das automatische setup erfolgt durch das Aufrufen des entsprechenden Bash-Scripts aus dem Projektverzeichnis, z.B. ````./Utils/setup.sh````.

**Manuelles Setup**

Sollte aus irgendeinem Grund ein manuelles Setup nötig sein, können die Schritte aus dem Setup Script manuell (ggf. selektiv) ausgeführt weren- Dies empfiehlt sich nur ebi entsprechenden Vorkenntnissen.

**Entwicklungs-Server**

Um die Anwendung zu Entwicklungszwecken laufen zu lassen bringt Django einen entsprechenden Webserver mit. *Dieser darf niemals zum Produktiveinsatz verwendet werden!*

Er wird gestartet durch ````python manage.py runserver```` aus dem Projektordner. Sofern wie im automatischen Setup ein Virtualenv verwendet wird, muss dieses aktiviert sein, über ````source venv/bin/activate````.

Der Entwicklungsserver kann dann im Browser über ````http://127.0.0.1:8000/```` aufgerufen werden.


### Produktions-Setup

Diese Anwendung kann mit einem Web-Server wie jede andere Django-Anwendung auch deployed werden.
Dabei muss ein secret kex verwendet werden, der nicht in einem Repository o.ä. liegt, und der DEBUG Modus in der ````settings.py```` deaktiviert werden.


### Updates

Um ein existierendes Setup auf den aktuellen Stand zu bringen kann das Update Script verwendet werden: ````./Utils/update.sh```` bzw. bei einem Produktivserver ````./Utils/update.sh --prod````.
