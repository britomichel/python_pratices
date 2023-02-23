# MyClassPerson_Super_And_AddProperty
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName( self ):
        print("Student:", self.firstName, self.lastName)

class Student( Person ):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
    
    def funcWelcome(self):
        print("Welcome", self.firstName, self.lastName, \
              "to the class of", self.graduationYear)

obj = Student("Mike", "Dee", 2023)
obj.printName()
print( "Graduation Year: " + str(obj.graduationYear) )

print()
obj.funcWelcome()
