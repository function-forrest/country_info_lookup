import requests

while True:
    country = input("Enter Country: ")
    url = f"https://restcountries.com/v3.1/name/{country}"

    if country:
        response = requests.get(url).json()
        if country.lower() == "quit" or country.lower() == "q":
            break
        country_info = response[0]
        capital = country_info["capital"][0]
        region = country_info["region"]
        population = country_info["population"]
        population = format(population, ",d")
        languages = country_info["languages"]
        languages = [languages[language] for language in languages]
        print(f"Capital: {capital}")
        print(f"Region: {region}")
        print(f"Population: {population}")
        print(f"Languages: {",".join(languages)}")
