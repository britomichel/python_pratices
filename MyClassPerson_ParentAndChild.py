# Herança / Inheritance

# - - - - - - - - - - - - - - - - - - - - - - - -
# - Parent class

class MyClassPerson_Parent:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print("Name:", self.firstname, self.lastname)


# - - - - - - - - - - - - - - - - - - - - - - - -
# - Child class (derived)

class MyClassPerson_Child( MyClassPerson_Parent ):

    pass

# - - - - - - - - - - - - - - - - - - - - - - - -

# using MyClassPerson_Parent class to create an object
myPerson = MyClassPerson_Parent("Matthew", "Kane")
print("myPerson printing...")
myPerson.printName()

# using MyClassPerson_Child class to create an object
myChild = MyClassPerson_Child("Hello", "Kitty")
print("myChild printing...")
myChild.printName()
