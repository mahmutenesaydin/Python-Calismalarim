myFile = open('movies.txt', 'r')

print(myFile.read())  #txt dosyasmızı okuyor
print(myFile.name)  #dosya adı
print(myFile.mode)  #dosyanın okuma modu

myFile.close()  #txt dosyasını kapattık
print(myFile.closed) #dosya kapanmışsa true, kapanmamışsa false döner





with open('movies.txt', 'r') as my_File:  #daha kullanışlı ve daha yaygındır, with'in içinden çıktıktan sonra oto kapatır 
    print(my_File.read())                 #her dosyayı açıp kapatmamıza gerek kalmıyor 'with'ciğim saolasın       
    print(my_File.read(20)) 
    print(my_File.readline(), end='')  #alt alta yazar
    print(my_File.readlines(), end='') #yan yana yazar


print(my_File.read())  #otomatik kapattığı için bu method çalışmaz 
print(my_File.closed)  #true çıkacak çünkü with'in içinden çıktıktan sonra otomatik kapatır

