cities = ['Suvaz','Liverpool','Madrid','Londra']
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
