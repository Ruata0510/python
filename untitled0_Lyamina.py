#111111111111111
a=1
b=10
for a in range(a,b+1):
    print(a)
    a+=1
#2222222222222222
a=int(input("Pl write"))
b=int(input("Pl write"))
if a<b:
    for a in range (a,b+1):
        print(a)
else:
    for a in range(a,b-1,-1):
        print(a)
#333333333333333333
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')