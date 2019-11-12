#111111111111111
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
#222222222222222
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
#333333333333333
n = int(input())
i = 2
nn = 1
while i <= n:
      i *= 2
      nn += 1
print(nn - 1, i // 2)
#444444444444444
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
#555555555555555
x = int(input())
p = int(input())
y = int(input())
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print(i)
#666666666666666
len = 0
while int(input()) != 0:
    len += 1
print(len)
#777777777777777
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)
#888888888888888
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)
#8888888888888888
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)
#99999999999999999
max = 0
index_of_max = -1
element = -1
len = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)
#101010101010101010
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1       
print(num_maximal)















