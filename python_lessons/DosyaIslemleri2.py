with open('data.txt', 'w') as myFile:
    myFile.write('Kuzgun\n')
    myFile.write('Icerde\n')
    print('Cukur', file=myFile)


with open('data.txt', 'a') as myFile:
    myFile.write('LCDP')

with open('data.txt', 'r') as myFile:
    print(myFile.read())



#Write(w) = var olan txt'nin üzerine yazar ve içindekileri siler
#Read(r) = txt dosyasının içindeki metinleri okur
#Append(a) = txt dosyasının içine yazar ve var olan metinleri silmez