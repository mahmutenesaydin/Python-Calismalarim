"""cities = ['Suvaz','Liverpool','Madrid','Londra']
for city in cities:   #listeyi yazdırdık
    print(city)  

for city in cities:
    print(f'Gezilen şehir: {city}')


for number in range(1,10):  #1-10 arasındaki rakamları yazdırır(1 dahil, 10 değil)
    print(number)

for number2 in range(2,21,2): #2 ile 21 arasındaki rakamları 2'şer arttırır(sondaki 2 o işe yarar)
    print(number2)

numbers = list(range(1,11))  #1-11 arasındaki rakamları liste olarak alır
print(numbers)

numbers = [number for number in range(1,11)] #For ile liste şeklinde sıralama yapıyoruz
print(numbers)

"""


#---------------------2.Video(17)--------------------

sayilar =[3,5,7,9,11]
for sayi in sayilar:
    print(sayi)

my_string = 'mhmtens'
for harf in my_string:
    print(harf)


for x in range(13,20,2): #sondaki 2 artış miktarını gösterir
    print(x)

friends = {'mahmut':21, 'mete': 20, 'berkin': 19, 'hasan':18}
for keyValue in friends.items():   #items yazarsak ikisini, key yazarsak stringi, value yazarsak değeri verir
    print(keyValue)

for key, value in friends.items():
    if key == 'berkin':
        break  #berkin olduğu zaman gerisini okumuyor sade berkine kadar okuyor
        continue #berkini bas geçiyor, okumadan geçiyor diğer elemanlara
    print(key, value)



arkidas = ['meteğ', 'berk"in', 'yeşil hasan', 'yunis']
for index, dost in enumerate(arkidas):
    print(index, dost)
