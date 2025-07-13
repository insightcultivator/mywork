# 변수와 데이터 타입
# 주석
print("Hello World!")  
# name = input("이름: ")
# print(name)

name = "홍길동"    # 문자열(str)
age = 25         # 정수(int)
height = 175.5   # 실수(float)
is_student = True  # 불리언(bool)

print(name,age,height,is_student)
print(type(name))

# 형변환
str(25)      # "25"
int("25")    # 25
print("타입은",type(int("25")))

s = "Python"
s[0]      # 'P' (첫 글자),인덱싱
s[0:3]    # 'Pyt' (슬라이싱)
print(s[2:])

# 메소드(함수랑 동일)
print(s.upper())      # 대문자로


upper = s.upper()
print(upper)


print(s.replace('y','i')) # 치환
print(s.split('t'))   # 분리


# 리스트 []: 순서 있음, 변경 가능
lst = [1, 2, 3]
lst.append(4)  # 추가
print(lst)
lst.remove(2)  # 제거
print(lst)
lst.sort(reverse=True)       # 정렬
print(lst)

# 튜플 (): 순서 있음, 변경 불가
tup,ss = (1, 2)
print(tup, ss)

# 딕셔너리 {}: 키-값 쌍
dic = {'name': '홍길동', 'age': 25, 'kk': 15}
dic['name']      # 값 접근
dic['height'] = 175  # 추가/수정
print(list(dic.keys()))       # 모든 키, values() 모든 값
print(list(dic.values()))
print(dic.items())      # 모든 키-값 쌍
for k,v in dic.items():
    print(k,v)
print(dic['kk'])
print(dic.get("kk","없는 값입니다"))    
# 집합(셋) {}: 중복 없음
st = {1, 2, 3}


