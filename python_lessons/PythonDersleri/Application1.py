#Alan ve çevreyi ondalıklı olarak hesaplayınız(import math)

r=5
pi=3,14159

print(pi*r*r)
print(pi*(r**2))
print(pi*(pow(r,2)))
print(round(2,pi*r,3))



import math  #matematik kütüphanesi

r=5
print(2*math.pi*r)


#-----------


# X için Tek mi Çift mi ?

x = 21
if(x % 2 == 0):
    print('çift')
else:
    print('tek')



# |4-7|*(4+7) = ?

print(abs(4 - 7) * (4 + 7))



#x='Suvazz' print(x), print(type(x))
x='Suvazz'
print(x)
print(type(x))

#-------
"""
name='mea'
My name is Arin with 3 method concatination, format, fstring
"""

name = 'mea'
print('My name is' + name)
print('My name is {}'.format(name))
print(f'My name is {name}')



#----
name = 'maho'
age = 21
married = True
print(age, name, married)



#-----------
x='100'
y=50
print(int(x) - y)




"""
Kullanıcıdan ismini al(input) ve büyük/küçük harfle yazdır
"""
nameee=input('ismin  nee?')
print(nameee.upper())
print(name.lower())
