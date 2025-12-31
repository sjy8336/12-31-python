""" 
[1]
국어, 영어, 수학 점수 입력받아
합계점수와 평균점수 구해 출력하기

평균점수가 >= 90 : A 학점
80점대 이면 : B
70점대 : C
60점재 : D
나머니 F학점
---------------------
국어      영어      수학
-----------------------
99        91       95
----------------------
합계점수:   점
평균점수:   점
학점: A
---------------------------------
"""

# [1]-내가 한거
""" kor = int(input('국어 점수를 입력하세요>>'))
eng = int(input('영어 점수를 입력하세요>>'))
math = int(input('수학 점수를 입력하세요>>'))
t = kor + eng + math
c = t / 3
d = ""
if c >= 90:
    d = "A"
elif 80 <= c < 90:
    d = "B"
elif 70 <= c < 80:
    d = "C"
elif 60 <= c < 70:
    d = "D"
else:
    d = "F"
s = f'''
국어: {kor}점
영어: {eng}점
수학: {math}점
--------------------------
합계점수: {t}점
평균점수: {c}점
학점: {d}
'''
print(s) """

"""
[2]
위에 입력받은 점수들 중 최소 점수를 구해서
과목명과 함께 출력하세요
최소 점수: 영어 91점
"""
# [2] - 내가 한거
""" k = "국어"
e = "영어"
m = "수학"
if kor < eng < math or kor < math < eng:
    print(f'최소 점수: {k} {kor}점')
elif eng < kor < math or eng < math < kor:
    print(f'최소 점수: {e} {eng}점')
else:
    print(f'최소 점수: {m} {math}점') """

kor = int(input('국어: '))
eng = int(input('영어: '))
math = int(input('수학: '))
total = kor + eng + math
avg = total / 3
grade = ''
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
else:
    grade = 'F'
# \t : tab키 만큼 띄워쓰기 함
s=f'''
국어\t영어\t수학
---------------------
{kor}\t{eng}\t{math}
---------------------
합계 점수: {total}점
평균 점수: {avg:.2f}점
학     점: {grade}
'''
print(s)

# 최소점수, subject: 최소점수 과목
mn = 9999
subject = ''
if mn > kor:
    mn = kor
    subject = '국어'
if mn > eng:
    mn = eng
    subject = '영어'
if mn > math:
    mn = math
    subject = '수학'
print(f'최소 점수: {mn}점 해당과목: {subject}')
# 국어 점수가 mn보다 작으니 mn에 국어점수가 반영되고
# 국어점수가 반영된 mn이 영어점수와 비교하게 되고
# 영어점수가 더 작으면 영어점수가 mn으로 대입되고
# 수학점수랑 비교하게 됨
# 근데 elif를 사용하면 if가 맞으면 통과하게 되니 다 if 적용한거임

# 최대 점수 구하기
mx = kor
subject = '국어'
if mx < eng:
    mx = eng
    subject = '영어'
if mx < math:
    mx = math
    subject = '수학'
print(f'최고 점수: {mx}점 해당과목: {subject}')