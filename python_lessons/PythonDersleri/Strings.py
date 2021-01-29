name = "imam sOfTwArE"

print(len(name)) #len = uzunluk
print(name[3]) #3.'de hangi harfin olduğu
print(name[2:8]) #3.'den 8.karaktere kadar olanları yaz
print(name.title()) #title = baş harfleri büyük gösterir
print(name.upper()) #upper = hepsini büyük harf gösterir
print(name.lower()) #lower = tüm harfleri küçük gösterir
print(name.count('m')) #count = girdiğimiz harfin(m) kaç tane olduğunu gösterir
print(name.find('O')) #find = girdiğimiz karakterimizin(O) kaçıncı harf olduğunu gösterir
print(name.replace('imam', 'maraz')) #replace = kelimeyi değiştirir

print(dir(name)) #string'de hangi parameteleri kullanabileceğimizi gösterir
print(help(str)) #hangi methodun ne işe yaradığını gösterir örnek gösterim 1 satır aşağıda da var
print(help(str.lower))