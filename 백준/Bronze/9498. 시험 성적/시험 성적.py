# A = map(int, input()) -> 이거는 문자열 하나하나를 숫자로 바꿈
# ex) 100을 입력하면 '1', '0', '0' 이 각각 정수로 변환됨!

# 지금원하는 건 100을 숫자로 변환해야 함
# input()은 값을 무조건 문자열(str)로 가져옴
# 밑에서 비교를 숫자랑 하기때문에 숫자로 변경해줘야 함! (int()로 감싸서)

A=int(input())

if 90 <= A <= 100 : #  if A>=90 and A<=100 도 가능!
    print("A")
elif A>=80 :
    print("B")
elif A>=70 :
    print("C")
elif A>=60:
    print("D")
else :
    print("F")
    
# + 팁 헷갈리면 중간에 주석을 달아서 구분해주자!
