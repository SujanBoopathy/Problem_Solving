class b1:
    def __init__(self):
        self.s1="hello"
        print("base1")
class b2:
    def __init__(self):
        self.s2="world"
        print("base2")

class derived(b1,b2):
    def __init__(self):
        b1.__init__(self)
        b2.__init__(self)
        print("derived")

obj=derived()
print(obj.s1+obj.s2)