# Tuple'dan 20 değern veren kodu oluşturun. aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])


#Grd lstes verldğnde, lstedek 4. sırak öğey kaldırav ve 2. konuma ekleyen kodu oluşturun
list = [34, 54, 67, 89, 11, 43, 94]
del list[4]
print(list)

list.insert(2,'11')
print(list)


# Verlen br strngde tüm küçük harf, büyük harf, rakam ve özel semboller sayısını veren kodu oluşturun.
input_str = ""
harf =  "P@#yn26at^&i5ve"
rakam =  "P@#yn26at^&i5ve"
karakter =  "P@#yn26at^&i5ve"


count=0
for a in harf: 
    if (a.isalpha()) == True: 
        count+=1
        input_str+=a 
print(count) 
print(input_str) 

count=0
for a in rakam: 
    if (a.isdigit()) == True: 
        count+=1
        input_str+=a 
print(count) 
print(input_str) 



# 4 le 40 arasındak tüm çft sayıların Python lstesn oluşturun
for sayi in range(4,40):
    if sayi % 2 == 0:
        print(sayi)



#Sayıların br lstes verldğnde,yalnızca 5'e bölüneblr sayıları yazdırın. Verlen lste : [10, 20, 33, 46, 55]
Liste = [10, 20, 33, 46, 55]

for sayilar in Liste:
    if sayilar % 5 == 0:
        print(sayilar)

