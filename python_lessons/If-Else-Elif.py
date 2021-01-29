age = 17
if age >=18:
    print('Oy kullan')
else:
    print('Ne oyu bebe')


my_list=['mahmut','enes','aydin']
if 'mahmut' in my_list:
    print('burada')



yas = 21
if yas <= 3:
    print('Tam İndirimli')
elif yas <= 12:
    print('Yarı indirimli')
else:
    print('Ne indirimi')



yasim = int(input('Sayı giriniz'))

if yasim <0:
    yasim = 0
    print('Eksi sayı olmaz')
elif yasim == 0:
    print('0 yaş değildir')
elif yasim <18:
    print('oy no')
else:
    print('yes oy')
