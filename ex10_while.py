# 반복문 (loop 문)
# for 루프
# while 루프
""" 
변수 선언 및 초기화
while 조건식:
    실행문장
    증가 또는 감소식
조건식이 True이면 while 루프 안의 블럭을 수행하고
False이면 반복문을 벗어난다
"""
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')

# Python을 5번 출력
i = 0
while i < 5:
    print('Python', i)
    # i = i + 1
    i += 1
print('-' * 50)
j = 10
while j > 0:
    print('bye', j)
    j -= 3  # j = j - 3
    # bye 10 7 4 1 -2
print('-' * 10, j)
# [1] While 문 이용해서 아래 값을 출력하기
# 1 3 5 7 9

# [1]
a = 1
while a <= 9:
    print(a, end=' ')
    a += 2
print('-' * 50)

# [2]
# 4 3 2 1 0

b = 4
while b >= 0:
    print(b, end=' ')
    b -= 1
print('-' * 50)

# [3] While문 이용해서 1부터 10까지의 합을 구하고 출력하기

c = 1
total = 0
while c < 11:
    total += c #c의 값을 누적 total = total + c
    c += 1
print('total: ', total)

""" 
문제
0부터 99까지 출력해 보세여
0부터 99까지 거꾸로 출력해보세요
0부터 99까지 합계를 구하세요
"""
""" x = 0
while x < 100:
    print(x, end='\t')
    x += 1
print('-' * 20) """

""" x = 0
while x < 100:
    print(a, end='\t')
    a += 1
    if a % 10 == 0:
        print() """

""" y = 99
while y >= 0:
    print(y, end='\t')
    y -= 1 """

y = 99
while y >= 0:
    print(y, end='\t')
    y -= 1

z = 0
t = 0

while z < 100:
    t += z
    z += 1
print(t)
print('-' * 60)

# [5] 1 ~ 50까지의 모든 정수 중 3의 배수만 출력하세요

q = 1
while q < 51:
    if q % 3 == 0:
        print(q, end='\t')
    q += 1
print()

# [6] 1 ~ 30 까지의 정수를 출력하되 아래와 같이 출력하세요
# 1 2 3 4 땅콩 6 7 8 9 찐콩 11 12 13 14 땅콩 16 17 18 19 찐콩...

w = 1
while w < 31:
    if w % 10 == 0:     #5부터하면 땅콩 찐콩 둘다 나오니 찐콩부터 해주고 나머지 5의 배수를 인식하게 해줌
        print('찐콩', end=' ') 
    elif w % 5 == 0:
        print('땅콩', end=' ') 
    else:
        print(w, end=' ')
    w += 1
print()

# [7] 구구단 중 특정 단을 input('몇 단?: ')함수로 입력받아
# 구구단 식과 결과값을 출력하세요

dan = int(input('구구단 몇단? : '))
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 지속적으로 바뀌는 부분만 변수를 준다
n = 1
while n < 10:
    print(f'{dan} x {n} = {dan * n}')
    n += 1