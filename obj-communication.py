class A(object):
    def sayHello(self,s):
        print("hello"+s)

class B(A):
    def __init__(self):
        self.obj=A()
    def sayHello2(self):
        self.obj.sayHello('sujan')

o=B()
print(o.sayHello2())
