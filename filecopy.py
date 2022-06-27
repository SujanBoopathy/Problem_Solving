import os.path
import sys
inp=open('input2.txt','r')

filename=input("Enter file name").strip()
if(os.path.isfile(filename)):
    print("file already exist")
    sys.exit()

out=open(filename,'w')

for line in inp:
    out.write(line)

out.close()

in2=open("output.txt",'r')
print(in2.read())