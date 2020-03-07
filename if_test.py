
# if 和 for
from math import sqrt
for count in range(0, 5):
    k = input('input the index of shape: ')
    if k == '1':
        print('circle')
    elif k == '2':
        print('oval')
    elif k == '3':
        sd1 = int(input('the first side: '))
        sd2 = int(input('the second side: '))
        if sd1 == sd2:
            print("the square's area is: ", sd1 * sd2)
        else:
            print("the rectangle's area is: ", sd1 * sd2)
    elif k == '4':
        print('triangle')
    else:
        print('you input invalid number')

# 列表 和 生成器
k = [i for i in range(10)]
j = [i + 1 for i in range(10) if i % 2 == 0]
o = (i + 1 for i in range(10) if i % 2 == 0)
print(k, j, o)

# while 和 break
sumA = 0
i = 1
while True:
    sumA += i
    i += 1
    if sumA > 10:
        break
print('i = {},sum = {}'.format(i, sumA))

# 输出素数
j = 2
while j <= 100:
    i = 2
    k = int(sqrt(j))
    while i <= k:
        if j % i == 0:
            break
        i += 1
    if i > k:
        print(j, end=' ')
    j += 1

# while 和 else
num = int(input('\nplease enter a number: '))
j = 2
while j <= int(sqrt(num)):
    if num % j == 0:
        print('{:d} is not a prime'.format(num))
        break
    j += 1
else:  # 如果循环正常结束，该else后的语句会被执行；
    print('{:d} is a prime'.format(num))

# 汉诺塔与递归
def hanoi(a, b, c, n):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a, c, b, n -1)
        print(a, '->', c)
        hanoi(b, a, c, n - 1)

hanoi('a', 'b', 'c', 7)
