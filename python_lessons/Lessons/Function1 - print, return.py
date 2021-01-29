def func(): #def, fonksiyon oluşturuken kullanacağımız kelime. Def'ten sonra func yazmak zorunda değiliz
    print("Hello World")
func()


def my_func(username):
    print(f'Hello {username}')
my_func("maho aga")


def funct(username, age=25): #değer verdiğimiz şey, default değerimizdir, bi değer girilmezse çalışır
    print(f'Hello {username}, {age} yaşındasın')
funct("maho", 21)



#RETURN

def func1():
    return 5+10

def func2():
    print(7+10)

result1 = func1()  #değer döndürdüğümüz için result'ı yazmaz, print'i yazar
result2 = func2()

print(f'Result 1, {result1}')  #böyle ise tam tersi print yazmaz, result'ı yazar 
print(f'Result 2, {result2}')


#----

def function():
    pass   #func'ımızın her hangi bir işlem yapmamasını sağlar, değer girsek de işlem yapmaz
function()
