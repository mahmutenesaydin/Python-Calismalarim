"""
'student' isminde class oluşturunuz
properties(attributes) = name, age, grades
notların(grades) ortalamasını gösteren method oluşturunuz
"""

class student:
    
    SchoolName='X Lisesi'  #Class değişkeni, tüm sınıflarda aynı olur buraya yazdığımız
    NumberOfStudents = 0

    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
        student.NumberOfStudents += 1

    def avarege(self):
        return sum(self.grades) / len(self.grades)

    def _schoolName(self):
        return f'Okulumuzun ismi {self.SchoolName}'

print(student.NumberOfStudents)

student1 = student('maho aga', 21, [20,40,70,90])

print(student.NumberOfStudents)

print(student1.avarege())
print(student1.SchoolName)
print(student1._schoolName())
print(student1.__dict__) #özellikleri ve o özelliklerin isimlerini yazar.    Örn= name : 'maho aga'
