""" while True:     #무한반복문
    # print('@@@@') """

# 무한루프 돌다가 특정 조건일 때 중단시키기
while True: 
    message = input('메세지 입력: ')
    if message == 'exit':
        break # 조건에 부합하면 반복문을 이탈함
    print(message)
print('bye bye ~~~')

# break : 가장 가까운 반복문을 벗어남
# continue : 특정 조건일 떼 skip하고 해당 반복문을 계속 수행함

num = 1
while num < 6:
    num += 1
    if num == 3:
        break
    print('num: ', num)
print('----------------------------')
num = 1
while num < 6:
    num += 1
    if num == 3:
        continue    #아래 문장을 skip하고 반복문을 계속 수행함
    print('num: ', num)
print('----------------------------')

# [1] 1 ~ 무한대 범위의 정수 합을 구하세요
#     단 이 정수의 합이 20000보다 크면 계산을 자동 중단하세요
#     총 합계를 출력

""" # [1] - 내가한거
a = 1
total = 0
while True:
    total += a
    a += 1
    if total > 20000:
        break
    print(total)
print('---------------------------') """

n = 1
total = 0
while True:
    total += n
    if total > 2000:
        break
    n += 1
print('total: ', total)

# [2] 1 ~ 100까지의 모든 정수의 합을 구하되
#     3의 배수와 7의 배수를 제외시키는 문장을 작성하세요

""" # [2] - 내가 한거
b = 1
tot = 0
while b < 101:
    tot += b
    b += 1
    if b % 3 == 0 or b % 7 == 0:
        continue
    print(tot) """

m = 0
tot = 0
while m < 100:
    m += 1
    if m % 3 == 0 or m % 7 == 0:
        continue
    print(m, end=', ')
    tot += m
print('tot: ', tot)