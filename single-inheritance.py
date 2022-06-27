class parrot:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name

class Bird(parrot):
    def sayHello(self):
        print("hello world")

b=Bird('parrot')
print(b.getName())
b.sayHello()



