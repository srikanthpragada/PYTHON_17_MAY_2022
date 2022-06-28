import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = country['name']['common']
    population = country['population']
    region = country['region']
    area = country['area']
    print(f"{name:50} {region:15} {population:10} {area:10}")

