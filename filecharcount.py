filename=input("Enter input filename :").strip()
fp=open(filename,'r')
s=""
for line in fp:
    s+=str(line.lower())



count=26*[0]

for i in s:
    if ord(i)<=ord('z') and ord(i)>=ord('a'):
        count[ord(i)-ord('a')] += 1

print(count)