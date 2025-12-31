""" 
[1]
아이디와 비밀번호를 입력받으세요
아이디가 scott이고 비밀번호가 tiger이면
"scott님 환영합니다"를 출력하고
아이디가 틀리거나 비밀번호가 일치하지 않으면
"로그인 실패!"를 출력하세요
"""
# [1] - 내가 한거
""" id = input('아이디를 입력하세요>>>>')
pw = input('비밀번호를 입력하세요>>>>')
if id == 'scott':
    if pw == 'tiger':
        print('scott님 환영합니다!')
    else:
        print('로그인 실패!')
else:
    print('로그인 실패!') """

# 같이 한거
userId = input('아이디: ')
userPw = input('비밀번호: ')
if userId == 'scott' and userPw == 'tiger':
    print(f'{userId}님 환영합니다')
else: 
    print('로그인 실패!')

"""
[2] 키와 몸무게를 입력받아 bmi 지수를 계산하세요
------------------------------------------
비만도 측정(BMI지수)
BMI를 이용한 비만도 계산은 자신의 몸무게를 키의 제곱으로 나누는 것으로
공식은 kg/m2. 
BMI가 18.5 이하면 저체중
18.5 ~ 22.9 사이면 정상
23.0 ~ 24.9 사이면 과체중
25.0 이상부터는 비만으로 판정.
신체질량지수
(BMI) = 체중(kg)/[신장(m)]2
------------------------------------------
""" 
# [2] - 내가 한거
''' cm = int(input('키를 입력해주세요 =>'))
kg = int(input('몸무게를 입력해주세요 =>'))
m= cm / 100
BMI = kg/(m**2)
if BMI <= 18.5:
    com = "저체중"
elif BMI <= 22.9:
    com = "정상"
elif BMI <= 24.9:
    com = "과체중"
else:
    com = "비만"
print(f"""
키: {m}
몸무게: {kg}
BMI: {BMI:.2f}
=> {com}
""") '''

w = int(input('몸무게(kg): '))
h = float(input('키(cm): '))
bmi = w / (h/100)**2
bmi = round(bmi, 1) #소수점 2자리에서 반올림
result=""
if bmi <= 18.5:
    result = "저체중"
elif bmi > 18.5 and bmi < 23:
    result = "정상 체중"
elif 23 <= bmi < 25:
    result = "과체중"
elif 25 <= bmi < 30:
    result = "비만"
else:
    result = "고도 비만"
s = f'''
몸무게 : {w}kg
키 : {h}cm
BMI지수 : {bmi}
당신은 {result}입니다
'''
print(s)

""" 
[3]
현재년도가 각각 1992, 2000, 2020과 (윤년o)
1900, 2100에 대해 (윤년x) 윤년여부를 출력하는
조건식을 작성하세요
윤년 : 4로 나눠 나머지가 0이고
    100으로 나눠 나머지가 0이 아니면
윤년 : 400으로 나눠 나머지가 0
"""
# [3] - 내가 한거
""" y = int(input('현재년도를 입력하세요>>>'))
x = y % 4
z = y % 100
v = y % 400
if x == 0:
    if z > 0:
        print(f'{y}년은 윤년입니다')
    else:
        print(f'{y}년은 윤년이 아닙니다')
elif v == 0:
    print(f'{y}년은 윤년입니다')
else:
    print(f'{y}년은 윤년이 아닙니다') """

year = 2025 #윤년
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("윤년 2월 29일까지 있어요")
else:
    print('평년 2월 28일까지 있어요')