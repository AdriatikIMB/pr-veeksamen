# 📋 Timeliste- og Brukerregistreringssystem

Dette prosjektet er et webbasert system utviklet med *Flask* som backend, og *HTML/CSS* med litt *JavaScript* på frontend. Systemet gjør det mulig å registrere brukere og føre timer for ansatte.

## 🚀 Funksjonalitet

### 🔐 Brukerregistrering

* Registrering av nye brukere gjennom et skjema.
* Følgende informasjon fylles inn:
  * **Brukernavn**
  * **Passord**
  * **Telefonnummer** (må starte med `+47` og ha 8 siffer etterpå)
* Informasjonen lagres i en MySQL-database i tabellen `test`.
* Feilhåndtering hvis brukernavnet allerede finnes.

### ⏱️ Timeregistrering

* Ansatte kan registrere arbeidstimer via et eget skjema.
* Følgende informasjon fylles inn:
  * **Prosjekt**
  * **Arbeidsleder**
  * **Prosent** (f.eks. 100%, 50%, 25%)
  * **Antall timer**
  * **Type timer** (vanlig, overtid, helg)
* Timer lagres i tabellen `timelister` i databasen.

### 🧭 Navigasjon

* Hver side har lenker som gjør det enkelt å navigere mellom forsiden, registrering og timeliste.

## 🗃️ Databasedesign

### Tabell: `test`

```sql
CREATE TABLE IF NOT EXISTS test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);


```sql
Kopier kode
CREATE TABLE IF NOT EXISTS timelister (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prosjekt VARCHAR(255) NOT NULL,
    arbeidsleder VARCHAR(255) NOT NULL,
    prosent INT NOT NULL,
    timer INT NOT NULL,
    type_timer VARCHAR(50) NOT NULL
);
🛠️ Teknologier brukt
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Database: MySQL

Server: Flask utviklingsserver

📂 Filstruktur
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
