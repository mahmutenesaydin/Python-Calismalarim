class student:

    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades  

    def avarege(self):
        return sum(self.grades) / len(self.grades)

student1 = student('maho aga', 21, [20,40,70,90])

class UniversityStudent(student):
    def __init__(self,name,age,grades,university):
        super().__init__(name, age, grades)
        self.university = university

uniStudent1 = UniversityStudent('mıho', 17, [10,20,30], 'ASU')

print(uniStudent1.university)
print(uniStudent1.age)
print(uniStudent1.name)
print(uniStudent1.avarege())

