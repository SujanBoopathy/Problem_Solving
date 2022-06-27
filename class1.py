class student:
    schl="gct"
    def __init__(self,name):
        self.name=name
    def getName(self):
        print(self.name)

s1=student('sujan')
print(s1.name)
print(s1.schl)

s2=student("saubali")
print(s2.name)
print(s2.schl)