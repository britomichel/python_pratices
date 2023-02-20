class MyClassPerson:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"str: {self.name}({self.age})"
    
    def funcSayHello(self):
        print("Hello! My name is", self.name, " and I'm", self.age, "old.")

myObjPerson = MyClassPerson("Matthew kane", 38)

print("myObjPerson.name:", myObjPerson.name)
print("myObjPerson.age:", myObjPerson.age)

print()

print( myObjPerson )
myObjPerson.funcSayHello()

print()

# atualizar atributo .age
myObjPerson.age = 40
print("Atualizou a idade (age) para 40 anos...")
myObjPerson.funcSayHello()

