# [1] 정수를 하나 입력받아 짝수이면 "Even" 홀수이면 "Odd"를 출력하세요

# 내가 일단 만든건데 못품
""" a = int(input('정수를 입력해주세요 =>'))
if a == 0 :
    print('Even')
else:
    print('Odd')
print('----------------------') """

# 같이 푼거
a = int(input('정수 입력 =>'))
# 2로 나눠서 나머지 값이 0 => 짝, 1 => 홀
x = a % 2
if x == 0:
    print('Even')
else:
    print('Odd')

# [2] 0 ~ 9999 사이의 정수를 입력받아 몇자리 수인지 알려주세요
# 15 ==> 2자리수
#  150 ==> 3자리수

# 내가 푼거
""" b = int(input('0 ~ 9999 사이의 정수를 입력하세요=>'))
if 10 > b >= 0:
    print('1자리수')
elif 100 > b > 9:
    print('2자리수')
elif 1000 > b > 99:
    print('3자리수')
else: 
    print('4자리수') """

num = int(input('0~9999사이 정수 입력>>'))
if num < 0 or num > 9999:
    print('입력 오류: 0~9999사이 정수여야 합니다')
else:   #유효한 값을 입력한 경우
    if 0 <= num < 10:
        print('1자리수입니다')
    elif 10 <= num < 100:
        print('2자리수입니다')
    elif 100 <= num < 1000:
        print('3자리수입니다')
    else:
        print('4자리수입니다')

# [3] 정수를 입력받고 입력받은 정수를 3으로 나눈 뒤
# 소수점 첫째 자리에서 반올림하기
#  입력값 : 10
#  출력값 : 3.3

# 내가 한거
""" c = int(input('정수를 입력하세요 =>'))
d = c % 3
e = c / 3
if d > 1:
    print('%d' %(c+1))
else:
    print('%d' %(c)) """

c = int(input('정수 입력>>'))
result = c / 3
print('result: ', result)
y = result - int(result)
print('y: ', y)
if y >= 0.5:
    result = int(result)+1
else:
    result = int(result)
print(result
)

print(int(round(c / 3, 0)))  #반올림 함수