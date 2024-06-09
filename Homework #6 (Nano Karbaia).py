# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება public, protected და private ცვლადები
# (მაგალითად ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე ზემოხსენებული მეთოდები.

from abc import ABC, abstractmethod


class Country(ABC):
    def __init__(self, name, continent):
        self.name=name
        self.continent=continent

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def capital(self):
        pass

    @abstractmethod
    def population_density(self):
        pass


class Georgia(Country):

    def __init__(self, name, continent, population, area, capital, religion):
        Country.__init__(self, name, continent)
        self._area = area
        self._capital = capital
        self._population = population
        self.religion=religion
        self.__budget = 'USD 8.25 billion'

    def area(self):
        print('Area of the Country: ', self._area)

    def capital(self):
        print('Capital of the Country: ', self._capital )

    def population_density(self):
        return self._population/self._area

    def budget(self):
        print(f'The Budget of the Country: {self.__budget}')

georgia=Georgia('Georgia', 'Europe', 3700000, 69700, 'Tbilisi', 'Orthodox Christianity')

print('Name of the Country: ', georgia.name)
print('Continent: ', georgia.continent)
print('Population of the Country: ', georgia._population)
print('Capital of the Country: ', georgia._capital)
georgia.capital()
print('Religion: ', georgia.religion)
print('Area of the Country: ', georgia._area)
georgia.area()
print('Population Density: ', georgia.population_density())
georgia.budget()
