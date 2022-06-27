import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for country in sorted(countries, key=lambda c: c['name']['common']):
    name = country['name']['common']
    # if capital key is missing then take capital as None
    capital = country.get('capital', ['None'])[0]
    capital = country.get('capital')[0] if 'capital' in country else 'None'
    print(f"{name:50} {capital}")

print(f"Found {len(countries)} countries")