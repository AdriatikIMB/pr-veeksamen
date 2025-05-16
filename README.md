# 📋 Timeliste- og Brukerregistreringssystem

Dette er et webbasert system hvor ansatte kan registrere sine arbeidstimer, og administrere sine kontoer. Systemet er bygget med *Flask* som backend og *HTML/CSS* med litt *JavaScript* på frontend.

## 🚀 Funksjonalitet

### 🔐 Brukerregistrering
1. Besøk **Forsiden**.
2. Klikk på **"Opprett konto"** for å registrere deg med et brukernavn, passord og telefonnummer (må starte med `+47`).
3. Hvis du allerede har en konto, kan du logge inn ved å bruke **brukernavn** og **passord**.

### ⏱️ Timeregistrering
1. Etter innlogging kan du registrere timer under "Registrer Timer".
2. Fyll inn informasjon om prosjekt, arbeidsleder, prosent, antall timer og type timer (vanlig, overtid, helg).
3. Når du sender inn skjemaet, får du en bekreftelse på at timene er registrert.

---

## 🧑‍💻 Hvordan bruke systemet

1. **Registrer deg som bruker:**
   - Gå til [Opprett konto](http://localhost:5000/createacc) og fyll inn brukernavn, passord og telefonnummer.
   - Hvis du allerede har en konto, kan du logge inn på [Innloggingsside](http://localhost:5000).
   
2. **Logg inn:**
   - Bruk ditt brukernavn og passord for å få tilgang til systemet.

3. **Registrer arbeidstimer:**
   - Gå til **Timeliste** for å registrere timer for prosjekter og arbeidsledere.

---

## 📂 Hvordan navigere i systemet
- **Forsiden**: Der du kan opprette en konto eller logge inn.
- **Opprett konto**: For å lage en ny bruker.
- **Timeliste**: For å registrere timer.

---

## 🛠️ Teknologier brukt
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Server:** Flask utviklingsserver (localhost:5000)

---

## ✍️ Forfatter
Systemet er utviklet av **Adriatik Veseli**. For mer informasjon, kan du kontakte utvikleren.


## Sikkerhet og forbedringer
✅ Eksisterende:

Enkel validering på HTML-skjema.

Telefonnummervalidering via regex.

## ⚠️ Anbefalte forbedringer:

Hashing av passord (eks. med werkzeug.security).

Bruk av Flask session for innlogging og autentisering.

CSRF-beskyttelse ved skjemaer (bruk Flask-WTF).

Input-sanitizing og feilhåndtering.

Legg til logger og audit trail for registreringer.

Utvid med brukerroller (admin/ansatt)

# 📋 Timeliste- og Brukerregistreringssystem - Utviklerdokumentasjon

Dette prosjektet er et webapplikasjon bygget med *Flask* som backend, og *HTML/CSS* med *JavaScript* på frontend. Det gir funksjonalitet for å registrere brukere og timelister, og lagre informasjon i en MySQL-database.

## 🚀 Komme i gang

### 1. Klon prosjektet
Start med å klone dette prosjektet til din lokale maskin.

```bash
git clone https://github.com/dittbrukernavn/timerregistrering.git
cd timerregistrering


2. Installer nødvendige avhengigheter
Prosjektet bruker Flask og MySQL-connector, så sørg for at du har disse installert:

bash
Kopier kode
pip install flask mysql-connector-python
3. Opprett MySQL-database
Opprett en MySQL-database og kjør SQL-skriptene for å sette opp nødvendige tabeller. Kjør disse kommandoene i MySQL:

sql
Kopier kode
CREATE DATABASE restaurant;

USE restaurant;

CREATE TABLE IF NOT EXISTS test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS timelister (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prosjekt VARCHAR(255) NOT NULL,
    arbeidsleder VARCHAR(255) NOT NULL,
    prosent INT NOT NULL,
    timer INT NOT NULL,
    type_timer VARCHAR(50) NOT NULL
);
4. Kjør Flask-appen
Start Flask-applikasjonen på din lokale utviklingsserver.

bash
Kopier kode
python app.py
5. Besøk systemet
Når serveren er startet, kan du gå til http://localhost:5000 i nettleseren.

🧑‍💻 Strukturen til prosjektet
Filstruktur
bash
Kopier kode
/templates
  ├── index.html
  ├── ansatt_timeliste.html
  ├── timeliste.html

/static
  └── js
      └── script.js

app.py
Forklaring av filene
/templates: Denne mappen inneholder HTML-malene for systemet.

index.html: Forsiden hvor brukeren kan registrere seg eller logge inn.
ansatt_timeliste.html: Skjema for ansatte til å registrere timer.
timeliste.html: Vist oversikt over registrerte timer.
/static/js: Inneholder JavaScript-filene som håndterer interaktiv funksjonalitet som bekreftelses-popup.
app.py: Flask-applikasjonen som håndterer routing, innlogging og databasen.

🛠️ Teknologier brukt
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Database: MySQL

Server: Flask utviklingsserver (localhost:5000)

📂 Funksjoner som er implementert
Brukerregistrering:
Brukeren kan opprette en konto med et unikt brukernavn, passord og telefonnummer.
Brukeren lagres i MySQL-databasen.

Innlogging:
Brukeren kan logge inn med brukernavn og passord.

Timeregistrering:
Ansatte kan registrere arbeidstimer, inkludert prosjekt, arbeidsleder, prosent og timer.
Bekreftelse:
Når timer er registrert, vises en bekreftelse via en JavaScript-popup.




