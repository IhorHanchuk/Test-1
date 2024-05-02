class Continent:
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def remove_country(self, country):
        self.countries.remove(country)


class Country:
    def __init__(self, name, area, population, capital):
        self.name = name
        self.area = area
        self.population = population
        self.capital = capital

    def display_info(self):
        print(f"Країна: {self.name}")
        print(f"Площа: {self.area} кв. км")
        print(f"Населення: {self.population}")
        print(f"Столиця: {self.capital}")


class DevelopedCountry(Country):
    def __init__(self, name, area, population, capital, gdp_per_capita, unemployment_rate):
        super().__init__(name, area, population, capital)
        self.gdp_per_capita = gdp_per_capita
        self.unemployment_rate = unemployment_rate


europe = Continent("Europe", 10180000, 747636000)
asia = Continent("Asia", 44579000, 4560000000)

ukraine = Country("Ukraine", 603500, 41902416, "Kyiv")
germany = DevelopedCountry("Germany", 357022, 83783942, "Berlin", 45260, 3.2)
china = DevelopedCountry("China", 9596961, 1403500365, "Beijing", 10261, 3.6)

europe.add_country(ukraine)
europe.add_country(germany)
asia.add_country(china)

print("Інформація про країни Європи:")
for country in europe.countries:
    country.display_info()

print("Інформація про країни Азії:")
for country in asia.countries:
    country.display_info()
