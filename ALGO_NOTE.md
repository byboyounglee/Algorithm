# 문제 풀이하며 내용 정리!


## 1330. 두 수 비교하기
1. if, elif, else 입력시 세로로 같은 라인으로 입력 

2. if ,elif, else 각각 뒤에 : 붙임

3. 처음에 split() 깜빡했는데 잘 기억해내서 풀음!

4. 삼항연산자로도 풀 수 있다고 함 (추후 더 공부)


## 9498. 시험 성적
1. A = map(int, input()) -> 이거는 문자열 하나하나를 숫자로 바꿈

   ex) 100을 입력하면 '1', '0', '0' 이 각각 정수로 변환됨!

3. 지금원하는 건 100을 숫자로 변환해야 함
4. input()은 값을 무조건 문자열(str)로 가져옴
5. 밑에서 비교를 숫자랑 하기때문에 숫자로 변경해줘야 함! (int()로 감싸서)
6. if 90 <= A <= 100 : 이걸로 한 번 해봤는데 맞았음! #  if A>=90 and A<=100 도 가능!
7.  팁 헷갈리면 중간에 주석을 달아서 구분해주자!



# 파일 위치 변경하는 방법
https://docs.github.com/ko/repositories/working-with-files/managing-files/moving-a-file-to-a-new-location
