#1111111111111111111
a=int(input())
b=int(input())
c=int(input())
if a>b>c:
   print(c)
elif a<b<c:
    print(a)
else:
    print(b)
#222222222222222222222
x = int(input())
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)
#3333333333333333333333
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
#4444444444444444444444
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#5555555555555555555555555
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
#66666666666666666666666
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
#7777777777777777777777
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES') 
else:
    print('NO')
#8888888888888888888888
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')
#9999999999999999999999999
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')
#10101010101010101010101010
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
#угадайка
import.random
a=random.randint(1,50)
h=int(input("сколько попыток будет?"))
g=0
while h>0:
    N=int(input("введи число от 1 до 50:"))
    if N<=50:
        if N==a:
            print("ты угадал")
            g+=1
        if h!=1:
            a=random.randint(1, 50)
    elif N<a:
            print("ставка ниже")
        else:
            print("ставка выше")
    else:
        print("вы ввели не коректное число")
    h-=1
    print("осталось попыток" ,h, "попыток")
print("загаданно было " ,a)
print("угадал " ,g, "раз")
    
 
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





