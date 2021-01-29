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

    @classmethod
    def DisplaySchoolName(cls, NameOfSchool):
        cls.SchoolName = NameOfSchool

    @staticmethod
    def static():
        return f'SelamunAleyküm'

student.DisplaySchoolName('Y Lisesi') 

student1 = student('maho aga', 21, [20,40,70,90])

print(student.SchoolName)
print(student1.SchoolName)

print(student.static())
print(student1.static())

