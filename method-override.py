class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("hwl")

class B(A):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("hello")

obj=B('sujan')
obj.show()
print(obj.name)