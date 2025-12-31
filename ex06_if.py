""" 
제어문
# 주 제어문
- 조건문 : if / if ~ else / if ~ elif ... else (다중 if)
- 반복문 : while, for
- 보조 제어문

# 보조 제어문
    : 주 제어문과 같이 사용됨 break, continue

[1]
if 문
if 조건식:
    실행문장

파이썬은 {}안에 실행문장을 넣는게 아니라서
들여쓰기 중요!!!

조건식이 True이면 실행문장을 실행함
"""
a = int(input('정수를 입력하세요=>'))
if a > 0:
    print(f'{a}는 양수입니다')
elif a == 0:
    print(f'{a}는 0입니다')
else:
    print(f'{a}는 음수입니다')
print("********************")

""" 
[2] if ~ else 문 사용
"""
if a > 10:  # True일 때 실행
    print('양수')
else:   # False일 때 실행
    print('0이거나 음수')
print("********************")   # 무조건 실행

""" 
다중 if문
if ~ elif ~ elif ~ else
"""
if a > 0:
    print('양수')
    print('####')
elif a == 0:
    print('제로')
    print('@@@@')
else:
    print('음수')
    print('&&&&')

