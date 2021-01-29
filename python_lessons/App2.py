dersler=['mat', 'beden', 'edb', 'biyo','kimya'] 

#ikinci elemanı büyük harfle al
print(dersler[1].upper())

#beden ve edb'in çıktısını al, ilk iki eleman çıktısını al, son iki eleman çıktısını al
print(dersler[1:3])
print(dersler[0:2])
print(dersler[-2:])

#Liste uzunluğunu göster, 'Tarih' dersini ekle, Coğrafya dersini ekle(2.yol)
print(len(dersler))
dersler.append('Tarih')
print(dersler)   
dersler[len(dersler):] = ['coğ']
print(dersler)

#insert ile ing dersini 2.sıraya ekle
dersler.insert(1,'ing')
print(dersler)

#beden dersini del, edb dersini remove yöntemiyle kaldır
del dersler[1]
print(dersler)
dersler.remove('edb')
print(dersler)



#--------

numbers = [10,8,58,34,41,9,7,17,88,77,99] 
#artacak ve azalacak şekilde sırala

numbers.sort() #artan
print(numbers)
numbers.reverse #azalan
print(numbers)


#-----------

lesson = [['mat', 'fizik'], ['beden', 'yazılım'], ['ardunio', 'wcf']]
#içteki listelerin son elemanlaryıla yeni bir liste oluşturalım

lesson2 = []
for ders in lesson:
    lesson2.append((ders[-1]))
print(lesson2)



#-------------
#1'den 10'a kadar olan sayıların karelerinden liste oluştur ve aynı işlemi list comprehension ile de yap

squares = []
for num in range(1,11):
    squares.append(num**2)
print(squares) 

squares2 = [num**2 for num in range(1,11)]  #list comprehension
print(squares2)