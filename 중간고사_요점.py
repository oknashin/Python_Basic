#  - type() 함수: ()안의 값의 type을 확인할 때 사용
print(type("Hello"))  # <class 'str'>
print(type(123))      # <class 'int'>

# - Type Ccasting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환

# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환
int_a = 3
float_b = 3.14
str_int_c = "9"
str_float_d = "9.2"
# 1) 문자열 정수형("9") -> 정수형 (9)
print(int(str_int_c))  # 9
# 2) 문자열 정수형("9") -> 실수형 (9.0)
print(float(str_int_c))  # 9.0
# 3) 문자형 실수형 ("9.2") -> 정수형 (Error: X)
# print(int(str_float_d))
# 4) 문자형 실수형 ("9.2") -> 실수형 (9.2)
print(float(str_float_d))  # 9.2
# 5) 정수형(3) -> 실수형 (3.0)
print(float(int_a))  # 3.0
# 6) 정수형(3) -> 문자열("3.0")
print(str(int_a))  # 3
# 7) 실수형(3,14) -> 정수형(3)
print(int(float_b))  # 3
# 8) 실수형(3.14) -> 문자열("3.14)
print(str(float_b))  # 3.14
# * float("Hello"), int("Hello") 형 변환 불가!

# None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
student_name = ""  # 사용법

# - 변수: "하나의 값"을 저장할 수 있는 메모리 공간
num = 4
num = 10
print(num)  # 출력: 10

# 동적 출력!
student_num = 20233107
student_name = "HyunWoo Shin"

# 1. format() 함수
print("조선대학교 {}, {}입니다.".format(student_num, student_name))

# 2. f-string - New
print(f"조선대학교 {student_num}, {student_name}입니다.")

# 문자 추출
#  - 인덱스틀 통해서 문자 추출
#  - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
print("="*100)
lang = "Python"
print(lang[0])  # p
print(lang[2])  # t
# print(lang[9]) Error
# -1 인덱스(Reverse Index)
#  - 우측에서 좌측으로 인덱스
#  - 시작값 -1
print(lang[-1])  # n
print(lang[-3])  # h

# 문자열 슬라이싱
#  - lang[3]: 문자 1개만 추출
#  - 부분 문자열을 추출하고 싶은 경우
#  - 시작인덱스, 끝인덱스 필요!
msg = "Python is all you need"
print(msg[0:6])  # 끝 인덱스+1  # Python
print(msg[:6])  # 시작 인덱스 생략 -> 자동 0 입력  # Python
print(msg[3:])  # 끝 인덱스 생략 -> 자동 -1 입력   # hon is all you need

# msg에서 "need"만 추출
# 정방향 인덱스 ->
# 역방향 인덱스 ->
print(msg[18:])  # need
print(msg[-4:])  # need

# 4.문자열 함수
str = "Hello World"

# 4-1.len() : 문자열 길이 계산
print(len(str))  # 11

# 리스트 초기화(생성)
print("="*100)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[0])    # 리스트에서 단일 값 추출  # chosun
print(list_c[1:3])  # 리스트 슬라이싱  # 98, 3.14

# 패킹과 언패킹
list_d = ["A", "B", "C"]  # 패킹
a, b, c = list_d  # 언패킹

# append(): 리스트 맨 마지막에 값 추가!
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)  # [1, 2, 3, 4, 5, 10]

# insert(): 원하는 인덱스에 값 추가!
a.insert(1,"A")  # (인덱스, 값)
print(a)  # [1, 'A', 2, 3, 4, 5, 10]

# extend(): 리스트 병합(List A + List B)
a = [1, 2, 3]
b = [3, 4, 5]
# a.append(b) -> [1, 2, 3, [3, 4, 5]]
# a.extend(b)  # a를 기준으로 병합
# print(a)
print(a + b)  # [1, 2, 3, 3, 4, 5]

# remove(값) : 값으로 삭제
a = ["a", "b", "c"]
a.remove("b")
print(a)  # ['a', 'c']

# pop(인덱스) : 인덱스로 삭제
b = ["a", "b", "c"]
c = b.pop(0) # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능!(선택사항)
print(b)  # ['b', 'c']
print(c)  # a

# index(): 찾고자 하는 값의 인덱스 반환
a = 1, 2, 3
print(a.index(3))  # 인덱스 반환  # 2

#  - sort(): 원본 값 정렬(주의: 보통 원본 값을 수정하는 경우 극히 드뭄)
#  - sorted(): 복제한 값 정렬
a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 오름차순
c = sorted(a, reverse=True)  #내림차순
print(a)    # [9, 3, 2, 1, 5, 8, 10]
print(b)    # [1, 2, 3, 5, 8, 9, 10]
print(c)    # [10, 9, 8, 5, 3, 2, 1]

# 튜플(Tuple): ex: 기차
# Tuple은 값 변경 불가능

a = [1, 2, 3]  # List
b = (1, 2, 3)  # Tuple
c = 1, 2, 3    # Tuple(가로 생략 가능)

a[0] = 99
print(a)  # [99, 2, 3]

# 튜플 원소가 1개인 경우
a = (1, 2, 3)  # tuple
b = 1, 2, 3    # tuple
c = (1)        # tuple
d = 1          # int
e = 1,         # tuple
print(type(b))  # <class 'tuple'>
print(type(d))  # <class 'int'>
print(type(e))  # <class 'tuple'>

# a랑 b랑 교환하는 코드 작성
# temp = a
# a = b
# b = temp
a = 5
b = 8
a, b = b, a  # Tuple packing & unpacking 사용
print(a)  # 8
print(b)  # 5

# 3.세트(Set) ex: 복주머니
#  - 순서 없음(index 없음, 정렬 불가능)
#  - 중복값을 허용하지 않음(중요)
set_a = {1, 2, 3}
set_b = {1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5}
print(set_b)  # {1, 2, 3, 4, 5}

# 중복값 제거 활용 방법
#  : a List의 중복값을 제거
a = ["A", "A", "B", "B", "C", "C", "D", "E"]  # List type
# List -> Set(중복값 제거) -> List
# a = set(a)        # ()안의 값을 set type으로 변환
# a = list(set(a))  # ()안의 값을 list type으로 변환
print(a)         # ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'E']
print(type(a))   # <class 'list'>

# 딕트(dict)  ex: 복주머니
#  - 순서가 없음(인덱스 없음, 정렬 불가능)
#  - {key : value} 사용 -> key, value 1 pair
#  - key는 중복 불가, value 중복 가능
#  - key를 통해서만 value에 접근 가능

dict_a = {"korea": "Seoul",
          "Canada": "Ottawa",
          "USA": "Washington D.C"}
print(dict_a)  # {'korea': 'Seoul', 'Canada': 'Ottawa', 'USA': 'Washington D.C'}
import pprint
pprint.pprint(dict_a)  # {'Canada': 'Ottawa', 'USA': 'Washington D.C', 'korea': 'Seoul'}

# update() : dict와 dict 병합
a = {"a": 1,
     "b": 2}
b = {"b": 3,
     "c": 5}
a.update(b)  # 병합시 중복key 있는 경우 입력값(b)이 우선
# pop() : dict 원소를 key를 통해서 삭제
c = a.pop("a")
print(a)  # {'b': 3, 'c': 5}
print(c)  # 1

# in() : ()안의 key값이 존재 확인
print("c" in a)  # True
print("f" in a)  # False

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션[index or key] ex: a[2]
# print(a["f"])    # key가 없으면 error 발생
print(a.get("f"))  # key가 없으면 None 출력(Error X)  # None

# keys(), values(), items()
print(a.keys())    # key만 추출         # dict_keys(['b', 'c'])
print(a.values())  # value만 추출       # dict_values([3, 5])
print(a.items())   # (key, value) 추출  # dict_items([('b', 3), ('c', 5)])

print(list(a.keys()))  # 활용 방법  # ['b', 'c']

# clear() : dict 초기화
print(a)  # {'b': 3, 'c': 5}
a.clear()
print(a)  # {}
e = {}
print(type(e))  # <class 'dict'>

# 조건문 4가지 조합
#   1. if
#   2. if~elif~elif
#   3. if~else
#   4. if~elif~else

# 점수계산기
#  - 91~100: A
#  - 81~90: B
#  - 71~80: C
#  - 61~70: D
#  - 60이하: F
print("="*100)
score = 95  # 0~100점
if score >= 91:
    print("A")
elif score >= 81:
    print("B")
elif score >= 71:
    print("C")
elif score >= 61:
    print("D")
else:
    print("F")

# 논리연산자: AND, OR, NOT

# 조건 1  조건 2  결과
#  F  and  F      F
#  T  and  F      F
#  F  and  T      F
#  T  and  T      T

# 2. OR
# 조건 1 조건 2  결과
#  F  or  F      F
#  F  or  F      F
#  F  or  F      F
#  F  or  F      F

# 3. NOT
# T -> F
# F -> T

# 문제 1. 어떤 종류의 학생인지 맞히기?
# (초등, 중등, 고등, 대학생, 학생 x)

from datetime import datetime

# input(): 키보드 값 입력 => string(문자열)
born = input("당신이 태어난 년도를 입력하세요: ")  # "2004
today = datetime.today().year
age = today - int(born) + 1  # 2023 - 2004 = 19
print(age)
if 0 <= age <= 26:
    if age <= 26 and age >= 20:
        print("대학생")
    elif age < 20 and age >= 17:
        print("고등학생")
    elif age < 17 and age >= 14:
        print("중학생")
    elif age < 14 and age >= 8:
        print("초등학생")

else:
    print("학생이 아닙니다.")

# 반복문(for, while)

# 반복횟수 o => for
# 반복횟수 x => while

# *for문 기본문법
#  for i in [1, 2, 3]:
#    print(i)

# *range() 함수
#  - default: 시작(0), 증감(+1)
#  - range(시작, 끝, 증감)
#  - range(3)       => 0, 1, 2
#  - range(1, 10)   => 1, 2, 3, 4, 5, 6, 7, 8, 9
#  - range(2, 5, 2) => 2, 4

# range()를 활용해서 1~9까지 출력하는 for문
for i in range(1, 10):
    print(i)    # 1~9

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)  # A~J

# *enumerate()
#  - 반복횟수(index) 출력하고 싶은 경우!
#  - enumerate() : 0번 인덱스부터 시작
for i, alpha in enumerate(temp):
    print(i+1, alpha)  # 1 A ~ 10 J

# dict를 사용한 for문
temp = {"A": 1,
        "B": 2,
        "C": 3,
        "D": 4}
# dict => for => Key값 출력
# keys(), values(), items()
for element in temp.values():
    print(element)   # 1, 2, 3, 4
for key, value in temp.items():
    print("*****")
    print(key)  # key   # A~D
    print(value)  # value  # 1~4

# break, continue
# break: 즉시 반복문을 빠져 나가세요.
# continue: 즉시 다음 반복으로 넘어가세요.

# a를 출력하다가 3을 만나면 멈추세요.
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)  # 1, 2

# 홀수만 출력
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5....29

print("="*100)

# while 반복문
#  - 반복횟수를 모르는 경우
#  - 조건이 만족하는 동안 계속 반복
#  - 조건 True이면 무한 반복
#  - 조건 False이면 반복 종료
#  - while문에 조건 True => 무한 Loop문(조심!!)
#    -> 반드시 break문과 함께 사용할것!

# while 기본 문법
# while 조건:
#     실행문

a = list(range(1, 6))  # [1, 2, 3, 4, 5]
print(a)

i = 0  # index
while i < len(a):
    print(a[i])  # 1~5
    i += 1

# 문제 1) 입력 된 단수를 출력하는 코드
dan = int(input("단수: "))
for i in range(1, 10):
    print(f"{dan}x{i}={dan*i}")

# 문제 2) 2단부터 9단까지 출력 => 중첩 for
# 2x1=2
# 2x2=4
# ...
# 2x9=18
# 3x1=3
# ...
# 9x9=81

# 2단 => 1~9
# 3단 => 1~9
# 4단
# 5단
# ...
# 9단

for i in range(2, 10):  # 2~9단(i)
    for j in range(1, 10):  # 단 내에서 1~9
        print(f"{i}x{j}={i*j}")

# 문제 3) list a의 평균값을 계산하세요.

a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total => 총합
total = 0
for num in a:
    total += num  # total = total + num
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result, 2))  # 평균값 24.18

# 문제 4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]
num_min = b[0]  # 최소값 담을 공간
for x in b:  # 5번 반복
    if x < num_min:
        num_min = x
print(num_min)  # 1 출력

# 문제 5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]
num_min = c[0]
num_max = c[0]
for x in c:
    if x < num_min:
        num_min = x
    if x > num_max:
        num_max = x
print(num_min)  # 1 출력
print(num_max)  # 8 출력

# 문제 6)사용자가 입력한 값 1, 2, 3 통과, 아닌 경우 다시 입력하도록

count = 0  # 틀린 횟수
while True:
    if count >= 3:
        print("프로그램을 사용할 수 없습니다.")
        break
    num = int(input("값: "))
    if num in [1, 2, 3]:
        print(f"{num}을 입력하셨습니다.")
        break
    else:
        print("1, 2, 3의값만 입력해주세요.")
        count += 1

# 문제7) 1부터 100까지 총합을 출력하는 코드
#  - for문으로 작성
total = 0
for num in range(1, 101):
    total += num
print(f"총합(for): {total}")   # 총합(for): 5050

#  - while문 작성
num = 0
total = 0
while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"총합(while): {total}")  # 총합(while): 5050

print("="*100)

# 함수 개발 가이드라인
# 함수 정의
#  1.기본 함수 문법
# def 함수명(parameter1, parameter2, ...):
#     실행문
#     return 반환값
def sub_two_value(x, y):
    n = x - y
    print(f"결과: {n}")  # 결과: -3
    return n

num = sub_two_value(5, 8)
print(num)  # 결과: -3

# 이름과 나이를 출력하는 함수

def print_info(name, age):
    print(f"이름: {name}, 나이: {age}")


name = input("이름: ")
age = int(input("나이: "))
print_info(name, age) # 이름과 나이를 출력하는 함수

#  - 만약에 함수호출시 입력해야하는 parameter가 empty인 경우
#    Default parameter로 대체해주는 기능!
# ex) def test(a=1, b=5, c=3):      (0)
# ex) def test(a, b=5, c=3):        (0)
# ex) def test(a, b, c=3):          (0)
# ex) def test(a=1, b, c):          (x)
# ex) def test(a, b=5, c):          (x)
# ex) def test(a=1, b=5, c):        (x)

# 소주 구매 가능 불가능 여부 확인
def soju_yn(age):
    if age >= 20:
        return 1  # 구매 가능
    else:
        return 0  # 구매 불가

age = int(input("나이: "))
result = soju_yn(age)
if result == 1:
    print("소주 구매가 가능합니다.")
elif result == 0:
    print("소주 구매가 불가능합니다.")

# 함수 내에서 함수 밖의 전역변수를 변경하고 싶은 경우?
#  return 반환값
a = 1  # 전역
print(a)  # 1 출력

def var_test(a):
    a = a+1  # 지역
    return a
a = var_test(3)
print(a)  # 4 출력

###############################################################
#  "스타벅스" 카페 키오스크 프로그램
#    - 일자: 2023년 10월 13일
#    - 작성자: oknashin
#    - 내용: 카페 음료를 주문 및 판매하는 콘솔 프로그램

# 조건
#  1.사용자는 최대 음료 1개, 베이커리 1개, 굿즈 1개 구매가능!

from service_kiosk import user_choice

# 메뉴와 가격표
#  - Dict Type -> 데이터베이스
main_name = {1: "음료(Drink)", 2: "빵 (Bakery)", 3: "굿즈(Goods)"}


drink_name = {1:"아메리카노", 2:"돌체콜드브루", 3:"딸기라떼", 4:"자몽에이드"}
bakery_name = {1:"카스테라", 2:"크로플", 3:"바움쿠헨"}
goods_name = {1:"텀블러", 2:"비치타월", 3:"무드등"}

drink_price = {1: 3000, 2: 4500, 3: 6000, 4: 5000}
bakery_price = {1: 4500, 2: 5000, 3: 7000}
goods_price = {1: 18000, 2: 7000, 3: 17000}

# 고객 주문 기록 저장
menu_save = []   # 고객 주문 메뉴 기록
price_save = []  # 고객 주문 금액 기록

# 1. 메인 메뉴 저장
print("■" * 20)
print("■■ == 스타벅스 ==")
print("■■ == ver 1.2 ")

while True:
    print("=" * 50)
    print("MSG: 만나서 반갑습니다. 고객님")
    print("■■ 메인 메뉴")
    for i in range(len(main_name)):
        print(f"■□  {i+1}.{main_name[i+1]}")
    print("■" * 20)

    # 2.메인 메뉴 선택
    choice = user_choice(len(main_name), "main")

    # 3.세부 메뉴 출력
    if choice == 1:    # 음료
        print("▲▲ 음료(Drink) 메뉴")
        for i in range(len(drink_name)):
            print(f"▲△  {i+1}.{drink_name[i+1]}({drink_price[i+1]})")
        # 4. 음료 세부 메뉴 선택
        sub = user_choice(len(drink_name), "sub")
        # 5. 음료 주문 저장
        menu_save.append(drink_name[sub])
        price_save.append(drink_price[sub])
    elif choice == 2:  # 빵
        print("▲▲ 빵(Bakery) 메뉴")
        for i in range(len(bakery_name)):
            print(f"▲△  {i+1}.{bakery_name[i+1]}({bakery_price[i+1]})")
        # 4. 빵 세부 메뉴 선택
        sub = user_choice(len(bakery_name), "sub")
        # 5. 빵 주문 저장
        menu_save.append(bakery_name[sub])
        price_save.append(bakery_price[sub])
    elif choice == 3:  # 굿즈
        print("▲▲ 굿즈(Goods) 메뉴")
        for i in range(len(goods_name)):
            print(f"▲△  {i+1}.{goods_name[i+1]}({goods_price[i+1]})")
        # 4.굿즈 세부 메뉴 선택
        sub = user_choice(len(goods_name), "sub")
        # 5.굿즈 주문 저장
        menu_save.append(goods_name[sub])
        price_save.append(goods_price[sub])
    elif choice == 99:
        print("MSG: 스타벅스 키오스크를 종료합니다.")
        exit()

    # 6. 추가 주문 or 결제 여부 선택
    print("●○추가 주문하시겠습니까?(y/n)")
    flag = 0  # 추가 주문 y/n
    while True:
        choice_yn = input("y/n: ")
        if choice_yn == "y" or choice_yn == "Y":
            break
        elif choice_yn.lower() == "n":
            flag = 1  # 주문 →결제창으로 이동
            break
        else:
            print("MSG: y 또는 n만 입력해주세요.")

    # 7. 주문내역 출력!
    if flag == 1:
        print("◆" * 50)
        print(f"◆◇ 고객님이 주문하신 메뉴")
        total_price = 0
        for i, menu in enumerate(menu_save):
            print(f"◆◇   {i + 1}.{menu}")
        for price in price_save:
            total_price += price
        print(f"MSG: 고객님이 주문하신 메뉴는 {len(menu_save)}개로 총 결제금액은 {total_price}원 입니다.")
        print(f"MSG: 이용해주셔서 감사합니다.")

def user_choice(max_cnt, menu_type):
    while True:
        choice = int(input(">> 번호: "))
        # main 메뉴에서 99를 입력하면 프로그램 종료!
        if choice == 99 and menu_type == "main":
            return choice
        # main or sub에서 메뉴 선택
        if max_cnt >= choice >= 1:
            return choice
        else:
            print("MSG: 올바른 번호를 입력하세요.")
