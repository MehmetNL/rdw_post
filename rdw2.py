import random
import requests
import string
from fastapi import FastAPI

api = FastAPI()

base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"


# Functie om RDW-gegevens op te halen
def get_rdw_data(kenteken):
    try:
        api_url = base_url + "?kenteken=" + kenteken.upper()
        api_voertuig = requests.get(api_url).json()
        if len(api_voertuig) == 0:
            return None  # Geen voertuig gevonden voor dit kenteken
        return api_voertuig[0]
    except Exception as e:
        print(f"Fout bij ophalen RDW-gegevens: {e}")
        return None


# Functie om kentekens te genereren
def genereer_kenteken():
    # Lijst van alle mogelijke Nederlandse kentekenformaten
    patronen = [
        "XX9999", "9999XX", "99XX99", "XXXX99",
        "99XXXX", "XX99XX", "X999XX", "XX999X",
        "X9999X", "XX9999", "9999XX", "9XX999",
        "XX999B", "B99999", "CD99999", "ZZ9999",
        "M999XX", "OV9999", "AA9999"
    ]

    # Kies een willekeurig patroon en genereer een kenteken
    patroon = random.choice(patronen)
    kenteken = ""
    for char in patroon:
        if char == "X":
            kenteken += random.choice(string.ascii_uppercase)  # Willekeurige hoofdletter
        elif char == "9":
            kenteken += str(random.randint(0, 9))  # Willekeurig cijfer
        else:
            kenteken += char  # Voeg streepjes toe
    return kenteken


# Bestand voor het opslaan van RDW-gegevens
output_file = "rdw_data.txt"

# Oneindige while-loop
while True:
    try:
        # Genereer een willekeurig kenteken
        kenteken_v1 = genereer_kenteken()

        # Haal RDW-gegevens op
        auto_1 = get_rdw_data(kenteken_v1)
        if not auto_1:
            print(f"Geen gegevens gevonden voor kenteken: {kenteken_v1}")
            continue

        # Extract informatie uit de API
        merk = auto_1.get("merk", "Onbekend")
        handelsbenaming = auto_1.get("handelsbenaming", "Onbekend")
        laatste_km_registratie = auto_1.get("jaar_laatste_registratie_tellerstand", "Onbekend")
        km_oordeel = auto_1.get("tellerstandoordeel", "Onbekend")

        # Print gegevens naar de console
        print(f"Kenteken: {kenteken_v1}")
        print(f"Merk auto: {merk}")
        print(f"Model auto: {handelsbenaming}")
        print(f"Laaste km stand registratie: {laatste_km_registratie}")
        print(f"Oordeel KM registratie: {km_oordeel}")
        print("-" * 50)
        
    except Exception as e:
        print(f"Fout in de hoofdloop: {e}")

