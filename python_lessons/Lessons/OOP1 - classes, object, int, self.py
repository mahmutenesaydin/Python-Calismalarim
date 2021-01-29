class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def BrandModel(self):
        return f'Arabanın markası {self.brand} ve modeli {self.model}'

car1=car('chery','tiggo',2009)
car2=car('land rover','freelander',1999)

print(car1)
print(car1.brand)
print(car2.year)
print(car1.BrandModel())