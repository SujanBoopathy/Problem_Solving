class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def getName(self):
        return self.name
    def getId(self):
        return self.id

class B(A):
    pass

class C(B):
    pass

o1=B('sujan',11)
o2=C('sauba',89)
print(o1.getId(),o1.getName())
print(o2.getId(),o2.getName())
print(o1.name)