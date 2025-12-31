# for 루프
# for 변수 in range([시작값], 종료값, [증가/감소치]) -> [] 생략가능한 것들
#   실행문
for i in range(5):  # 시작(0), 종료: 5~1까지, 증가치: 1씩 증가
    print('Welcome to everyone : ', i)

for j in range(1, 10, 2):   #시작:1, 종료: 9, 증가치: 2
    print('Be Happy~', j)

# [1] 1 ~ 50까지의 중수 중 7의 배수만 출력 for루프 이용
""" for a in range(1, 51, 1):
    if a % 7 != 0:
        continue
    print(a) """

for k in range(1, 51):
    if k % 7 == 0:
        print(k, end=', ')
print('------------------------')

# [2] 0 ~ 9사이의 정수를 거꾸로 출력해보세요
""" for b in range(9, 0, -1):
    print(b)
print('------------------------') """

for j in range(9, -1, -1):
    print(j, end = ' ')
print('------------------------')

# reversed(range(n))함수
for x in reversed(range(10)):
    print(x, end=' ')
print('------------------------')


# [3] 1 ~ 10까지의 합을 구하되 덧셈식도 같이 출력하세요
# 1+2+3+4+5+6+....+10=55
""" t = 0
for c in range(1, 11, 1):
    print(c)
    t += c
print(t) """

total = 0
for y in range(1, 11):
    if y < 10:
        print(y, end='+')
    else:
        print(y, end='=')
    total += y
print(total)