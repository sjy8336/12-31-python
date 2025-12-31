# for 변수 in 리스트:
# list ==> iterable객체
lst = [10, 20, 30]
for i in lst:
    print(i, end=' ')
print()

# for 변수 in 문자열:
# 문자열 첫 문자부터 끝 문자까지 순차적으로 변수에 전달된다
# 문자 개수만큼 반복 실행됨
for s in "Hello Python":
    print(s, end=', ')
print()