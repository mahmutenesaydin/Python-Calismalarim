import myModule     #başka py dosyasındaki kodları burada çalıştırabiliriz import sağolsun

numbers = [1,2,3,4,5]
sum = myModule.summation(numbers)

print(sum)



    
from myModule import myString, summation
numbers = [10,20,30]
sum = summation(numbers)

print(sum)
print(myString)




import math
print(math.pi)



import random
number = [3,6,9,12]
randomNumber = random.choice(number)
print(randomNumber)