#tuple
capitals = ('ist', 'sivas', 'kocaeli','kayseri')
print(capitals)
capitals=('roma', 'londra')
print(capitals)

#--tuple'de () kullanılır, set'de {} kullanılır


#set
cities = {'ist', 'sivas', 'kocaeli','kayseri'}
print(type(cities))
print(cities)

cities.add("malatya") #set'e tek eleman eklerken add
print(cities)

cities.update(['rize','trabzon']) #çok eleman eklerken update kullanılır
print(cities)

cities.remove('kayseri')
print(cities)

cities.clear()
print(cities)  #Set'imizin tamamını siler