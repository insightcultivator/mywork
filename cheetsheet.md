### 1. 변수와 데이터 타입
```python
# 주석
print("Hello World!")  # 출력
name = input("이름: ")  # 입력

name = "홍길동"    # 문자열(str)
age = 25         # 정수(int)
height = 175.5   # 실수(float)
is_student = True  # 불리언(bool)

# 형변환
str(25)      # "25"
int("25")    # 25
```

### 2. 연산자
```python
# 산술: +, -, *, /, //(몫), %(나머지), **(제곱)
# 비교: ==, !=, >, >=, <, <=
# 논리: and, or, not
```

### 3. 문자열
```python
s = "Python"
s[0]      # 'P' (첫 글자)
s[0:3]    # 'Pyt' (슬라이싱)

# 메소드
s.upper()      # 대문자로
s.replace('y','i') # 치환
s.split('t')   # 분리
```

### 4.컬렉션(Collection)
```python
# 리스트 []: 순서 있음, 변경 가능
lst = [1, 2, 3]
lst.append(4)    # 추가
lst.remove(2)    # 제거
lst.sort()       # 정렬

# 튜플 (): 순서 있음, 변경 불가
tup = (1, 2, 3)

# 딕셔너리 {}: 키-값 쌍
dic = {'name': '홍길동', 'age': 25}
dic['name']      # 값 접근
dic['height'] = 175  # 추가/수정
dic.keys()       # 모든 키, values() 모든 값
dic.items()      # 모든 키-값 쌍

# 집합(셋) {}: 중복 없음
st = {1, 2, 3}
```

### 5. 제어문
```python
# 조건문
if x > 0:
    print("양수")
elif x == 0:
    print("영")
else:
    print("음수")

# for 반복문
for item in [1,2,3]:
    print(item)

# while 반복문
i = 0
while i < 5:
    print(i)
    i += 1
```

### 6. 함수
```python
# 함수 정의
def greet(name):
    return f"안녕, {name}!"

# 함수 호출
greet("홍길동")  # "안녕, 홍길동!"

# 기본값 매개변수
def greet(name="친구"):
    return f"안녕, {name}!"
```

### 7. 클래스
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"안녕, {self.name}!"

p = Person("홍길동", 25)
p.name  # "홍길동"
p.greet()  # "안녕, 홍길동!"
```

### 8. 예외 처리
```python
try:
    x = int(input("숫자: "))
except ValueError:
    print("숫자가 아닙니다")
```

### 9. 모듈 및 라이브러리
```python
# 내장 모듈
import math
math.sqrt(16)  # 4.0

# 부분 임포트
from random import randint
randint(1, 10)  # 1~10 사이 난수

# 외부 라이브러리
# pip install numpy
import numpy as np
```

### 10. 파일 처리
```python
# 파일 읽기
with open('file.txt', 'r') as f:
    data = f.read()

# 파일 쓰기
with open('file.txt', 'w') as f:
    f.write('Hello')
```
