import os
import requests
import pandas as pd
from sdtp import RowTable

# 1. Internal K8S Path & Auth
PUBLISH_URL = "http://galyleo-service.jhub-kct-free.svc.cluster.local:5000/services/galyleo/publish_data"
API_TOKEN = os.getenv('JUPYTERHUB_API_TOKEN')

# 2. Global Station IDs for 2023
STATIONS = {
    "London": "03772099999",
    "Tokyo": "47662099999",
    "Beijing": "54511099999",
    "Sydney": "94767099999",
    "Rio": "83746099999"
}

# 3. Read the NOAA Climate Data for the selected cities
all_data = []
for city, sid in STATIONS.items():
    url = f"https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2023/{sid}.csv"
    df = pd.read_csv(url)[['DATE', 'TEMP', 'PRCP']]
    df['CITY'] = city
    all_data.append(df)

final_df = pd.concat(all_data)

# 4. SDML Schema - Explicitly typed for the Galyleo Service
schema = [
    {"name": "DATE", "type": "date"},
    {"name": "TEMP", "type": "number"},
    {"name": "PRCP", "type": "number"},
    {"name": "CITY", "type": "string"}
]

# 5. Publish Directly
table = RowTable(schema, final_df.values.tolist())
headers = {'Authorization': f'token {API_TOKEN}'}
r = requests.post(PUBLISH_URL, headers=headers, json={
    "table": table.to_dictionary(),
    "name": "global_weather_tutorial.sdml"
})

print(f"Status: {r.status_code} - Global Weather Published!" if r.ok else f"Failed: {r.text}")