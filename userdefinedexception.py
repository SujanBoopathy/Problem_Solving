class errorCode(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data

try:
    raise errorCode(3838)
except errorCode as e:
    print(e.data)