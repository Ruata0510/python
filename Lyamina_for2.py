#111111111111111
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)
#222222222222222
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
#3333333333333333
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
#4444444444444444
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)
#55555555555555555
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
#66666666666666666
n = int(input())
 
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
 
print(sum)
#7777777777777777
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)
#8888888888888888
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
#9999999999999999999
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)
#101010101010101010
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
#11111111111111111
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
# можно доказать формулу:
# sum == n * (n + 1) // 2
# но мы посчитаем это значение циклом
for i in range(n - 1):
    sum -= int(input())
print(sum)























