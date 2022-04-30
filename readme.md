# EV3 Robotics ~ Max Born Berufskolleg



# Inhaltsverzeichnis
1. [Installation](#Installation)
1. [Konfiguration](#Konfiguration)
2. [Ev3Dev Browser](#ev3dev-browser)
# Installation
## Was wird installiert?
- [Choco](https://chocolatey.org/)
- [Python](https://www.python.org/)
- [PyBricks](https://pypi.org/project/pybricks/)
- [VS Code](https://code.visualstudio.com/)
  
## Durchführung
1. Diese Repository als ZIP-Archiv herunterladen
2. Das ZIP-Archiv in einem beliebigen Ordner entpacken
3. Powershell im Verzeichnis öffnen
4. Eine der folgende Befehle ausführen:
   - Für Windows-Benutzer: <br>` powershell ./install.ps1`
   - Für Linux-Benutzer: kommt noch

# Konfiguration
## VS Code
1. Öffne VS Code
2. Lade folgende Erweiterungen in VS Code herunter:
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [PyBricks](https://marketplace.visualstudio.com/items?itemName=ms-vscode.pybricks)
   - [Ev3Dev Browser](https://marketplace.visualstudio.com/items?itemName=ev3dev.ev3dev-browser)

# EV3dev Browser 
EV3dev Browser ist ein Browser für die EV3-Bricks. <br> Das heißt, dass Sie durch Bluetooth/USB/WIFI mit dem EV3-Brick kommunizieren können und scripts in EV3-Brick ausführen können.
## Vorbereitung
### Bluetooth
    Stellen Sie sicher, dass Sie die Bluetooth-Einstellungen des EV3-Brick richtig konfiguriert haben und mit Ihrem Laptop verbunden haben. 
### USB
      Einfach den EV3-Brick durch USB-Anschluss anschließen.

## Anwendung

Damit Sie mit dem EV3-Brick kommunizieren können, müssen Sie ein paar Befehle ausführen.

1. In VS Code klicken Sie auf die Tasten `STRG + ALT + P` oder `F1`
2. Schreibe "ev3dev"
3. Klicken Sie auf die `ev3dev: Connect to a device`
4. Dann wählen Sie den EV3-Brick aus

Und nun wird das EV3-Brick unter `EV3DEV DEVICE BROWSER`  angezeigt. Welche sich unten Links in VScode befindet.


# Skripte auf Brick vom Computer ausführen
Einfach `F5` drücken und das Skript wird ausgeführt.

