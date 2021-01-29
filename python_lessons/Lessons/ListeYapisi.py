
cities = ['Suvaz','ist','kocaeli','urfa']

print(cities[0])
print(len(cities)) #uzunluk
print(cities[0:2]) #0-2 arasındaki şehirler(0 dahil, 2 dahil değil)

#---ekleme işlemleri---
cities[3] = 'gayseri'  #Listedeki elemanla, değiştirme işlemi yapar(urfa yerine gayseri)
print(cities)

cities.append('malatya') #listeye ekleme işlemi yapar, malatyayı listeye ekler
print(cities)

cities.insert(2,'Bolu') #Önce eklemek istediğim yeri sonra da eklemek istediğimizi yazıyoruz 'insert'
print(cities) 

#---silme işlemleri---
del cities[3] #Silme işlemidir. 'del' yöntemi ile sildiğimiz şeye daha ulaşamayız
print(cities)

cities.pop() #Buda silme işlemidir ve 'pop' yöntemi ile sildiğimiz şeye ulaşırız
print(cities)

cities2=cities.pop()#sildiğimiz sondaki şehire ulaştık
print(cities2)

cities.remove('ist') #'Remove' methodu da silme işlemi yapar 
print(cities)


#---sıralama işlemleri---
cities.sort() #Alfabetik olarak sıralama işlemi yapar(A->Z)
print(cities)

cities.sort(reverse=True) #Alfabenin tersi şeklinde sıralama yapar(Z->A)
print(cities)

print(sorted(cities)) #Listeyi geçiçi olarak(o anlık) alfabe sırasına göre alır

numbers = [34,58,7,17,77,88,18,8]
print(min(numbers)) #min sayı
print(max(numbers)) #max sayı
print(sum(numbers)) #toplam








#-----------Liste 2.video----------

cities = ['Suvaz','Liverpool','Madrid','Londra']
print(cities.index('Madrid')) #madrid'in kaçıncı sırada(index'de) olduğunu öğrenmemizi sağlar

print('ankara' in cities) #ankara'nın listede olup olmadığını inceliyoruz

str_email = 'mhmtens13@gmail.com'
my_list = str_email.split('@')   #listeyi @ işaretine göre ayıracak(@'den önce ve sonra)
print(my_list)

cities2 = cities[:]  #birbine eşitledik yani aynı liste oldu(: koyduğumuz için sonradan eklediğimizi almadı)
print(cities2)
cities.append('Artvin')
print(cities)
print(cities2)

