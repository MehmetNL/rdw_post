import requests
from fastapi import Request, FastAPI

api = FastAPI()

base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"


@api.get('/rdw')
def get_rdw_data(kenteken):
    api_url = base_url + "?kenteken=" + kenteken.upper()
    api_voertuig = requests.get(api_url).json()
    voorbeeld = api_voertuig[0]

    # print(vooorbeeld["merk"])
    # return vooorbeeld["merk"]
    return voorbeeld


auto_1 = get_rdw_data("P300BB")

print(f"Merk auto: {auto_1["merk"]}")
print(f"Model auto: {auto_1["handelsbenaming"]}")
print(f"Laaste km stand registratie: {auto_1["jaar_laatste_registratie_tellerstand"]}")
print(f"Oordel KM registratie: {auto_1["tellerstandoordeel"]}")
