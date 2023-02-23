# MyClassPerson_Super_And_AddProperty
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName( self ):
        print("Student:", self.firstName, self.lastName)

class Student( Person ):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2023

obj = Student("Mike", "Dee")
obj.printName()
print( "Graduation Year: " + str(obj.graduationYear) )
