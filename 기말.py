# 필기: Lecture 폴더 1, 2, 3, 7, 8, 9 에서만 출제

# 실기: 3문제

#   2번~3번 문제: 주말에 예제 문제를 업로드 비슷하게 내기

# 1번문제: 웹 크롤링(selenium)
#   - (베이스라인 코드 제공) -> select()[0].get_text() 등등 위주로 공부할 것!
#   - 베이스라인 코드는 드리지만 중간중간 기존 코드에서 삭제 된 부분이 있습니다. 해당 부분은 스스로 채우셔서 코드가 동작하게 하셔야 합니다.
#     셀레니움과 beautifulsoup4를 사용해서 웹 크롤링하는 과정을 이해하시면 충분히 해결 할 수 있는 수준으로 출제됩니다.

# 2번문제: 별찍기 관련 문제
#
#   - 과제로 풀어봤던 별찍기를 응용해서 해결할 수 있는 문제

for i in range(1, 6):
  for j in range(i):
    print('*', end='')
  print()

# 3번문제: 함수 생성 및 호출, return에 관한 문제

#   - 조건에 맞는 함수를 생성
#   - 생성한 함수 호출
#   - 함수로부터 반환값을 받아 출력 등
# ----------------------------------------------------------------------------------------------------------------------

# 출력 함수(print)
# - ()안의 값을 출력
# - 변수 값 확인 용도 또는 메세지 출력 용도
print("=" * 200)
print("Hello Python")

# 문자열 타입(String Type)
# - Python: '', "" -> String
# - C, JAVA: ''(Char), ""(String)

# 자료형(type)
# - Python의 모든 자료형은 객체(Object)
# - C, Java 언어 문자형(char): 'A', 'E' = 키보드 제어
# 1) 문자열(String): "Hello", 'Hi'
# 2) 정수형(int): 3, 0, -1
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

#  - type() 함수: ()안의 값의 type을 확인할 때 사용
print("=" * 200)
print(type("Hello"))
print(type(123))

# 형 변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환

# * 문자형 실수형 ("9.2") -> 정수형 (Error: X)
# * float("Hello"), int("Hello") 형 변환 불가!

# None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
# - 기타 언어의 Null과 같은 의미로 사용!

# 기본자료형(Primitive Type) : 변수에 값이 저장
#  - int num = 4;
# 객체자료형(Reference Type) : 변수에 값의 "주소"가 저장
#  - String name = "10";

# 변수(Variable)
# - 변수: "하나의 값"을 저장할 수 있는 메모리 공간
num = 4
num = 10
print(num)  # 출력: 10

# 대입연산자(=) : 우측의 값을 좌축에 저장
# 동등연산자(==) : Equal

# 동적 출력!
print("=" * 200)
student_num = 20233107
student_name = "HyunWoo Shin"

# 출력 예: "조선대학교 20233107, HyunWoo Shin 입니다."
print("조선대학교 20233107, HyunWoo Shin 입니다.")  # 하드 코딩 지양!

# 1. format() 함수
print("조선대학교 {}, {}입니다.".format(student_num, student_name))

# 2. f-string - New
print(f"조선대학교 {student_num}, {student_name}입니다.")


# 간단한 사칙연산
#  + : 더하기
#  - : 빼기
#  * : 곱하기
#  ** or 2: 제곱
#  5/2 : 나누기          2.5
#  5//2 : 나누기(몫)     2
#  5%2 : 나누기(나머지)  1

# 문제?
num = 9
num - 1
num + 2
print(num)

# 1. 문자열 인덱스
#  - 문자열은 각 문자마다 순서(인덱스)가 있음
#  - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#  - 인덱스 시작은 0
#  - 인덱스는 공백 포함

# 2.문자 추출
#  - 인덱스틀 통해서 문자 추출
#  - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9]) Error
# -1 인덱스(Reverse Index)
#  - 우측에서 좌측으로 인덱스
#  - 시작값 -1
print(lang[-1])
print(lang[-3])

# 3. 문자열 슬라이싱
#  - lang[3]: 문자 1개만 추출
#  - 부분 문자열을 추출하고 싶은 경우
#  - 시작인덱스, 끝인덱스 필요!
msg = "Python is all you need"
print(msg[0:6])  # 끝 인덱스+1
print(msg[:6])  # 시작 인덱스 생략 -> 자동 0 입력
print(msg[3:])  # 끝 인덱스 생략 -> 자동 -1 입력

# 4.문자열 함수
str = "Hello World"

# 4-1.len() : 문자열 길이 계산
print(len(str))

# 컬렉션 타입
#  - 변수 하나에 값을 여러개 저장
#  - 실질적으로 변수에 컬렉션 1개가 저장
#  - 리스트(List), 튜플(Tuple), 딕트 (Dictionary), 세트(set)

# 1. 리스트(List)  ex)  기차!
#  - 시퀸스 자료형 (연속된 값 저장)
#  - 대가로 사용 []
#  - 정렬 가능
#  - mutable(생성된 후 변경 가능)
#  - index 사용 (Slicing 가능)
#  - paking과 unpaking 가능
#  - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), 등등
# * 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[0])    # 리스트에서 단일 값 추출
print(list_c[1:3])  # 리스트 슬라이싱

# 패킹과 언패킹
list_d = ["A", "B", "C"]  # 패킹
a, b, c = list_d  # 언패킹

# append(): 리스트 맨 마지막에 값 추가!
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)

# insert(): 원하는 인덱스에 값 추가!
a.insert(1,"A")  # (인덱스, 값)
print(a)


# extend(): 리스트 병합(List A + List B)
a = [1, 2, 3]
b = [3, 4, 5]
# a.append(b) -> [1, 2, 3, [3, 4, 5]]
# a.extend(b)  # a를 기준으로 병합
# print(a)
print(a + b)

# remove(값) : 값으로 삭제
a = ["a", "b", "c"]
a.remove("b")
print(a)

# pop(인덱스) : 인덱스로 삭제
b = ["a", "b", "c"]
c = b.pop(0) # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능!(선택사항)
print(b)
print(c)

# index(): 찾고자 하는 값의 인덱스 반환
a = 1, 2, 3
print(a.index(3))  # 인덱스 반환

# sort() and sorted(): 리스트 값 정렬!
#  - sort(): 원본 값 정렬(주의: 보통 원본 값을 수정하는 경우 극히 드뭄)
#  - sorted(): 복제한 값 정렬
a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 오름차순
c = sorted(a, reverse=True)  #내림차순
print(a)
print(b)
print(c)

# 2. 튜플(Tuple): ex: 기차
#  - List와 대부분 동일
#  - 시퀀스 자료형(정렬 불가능)
#  - immutable(생성 된 후 변경 불가능)
#  - index 사용(Slicing 가능)
#  - packing과 Unpacking 가능
#  - () 사용(생략 가능)
#  * 여러분이 직접 tuple을 생성하는 경우 x
#    -> 파이썬에서 결과값을 받을 때 Tuple로 제공

print("="*100)
a = [1, 2, 3]  # List
b = (1, 2, 3)  # Tuple
c = 1, 2, 3    # Tuple(가로 생략 가능)

a[0] = 99
print(a)

# b[0] = 99
# print(b)  # Tuple은 값 변경 불가능

# 튜플 원소가 1개인 경우
a = (1, 2, 3)  # tuple
b = 1, 2, 3    # tuple
c = (1)        # tuple
d = 1          # int
e = 1,         # tuple
print(type(b))
print(type(d))
print(type(e))

a = 5
b = 8

# a랑 b랑 교환하는 코드 작성
# temp = a
# a = b
# b = temp
a, b = b, a  # Tuple packing & unpacking 사용
print(a)  # 8
print(b)  # 5

# 3.세트(Set) ex: 복주머니
#  - 수학의 집합 개념
#  - 순서 없음(index 없음, 정렬 불가능)
#  - 중복값을 허용하지 않음(중요)
#  - {} 사용
#  - 멤버함수: union(), intersection(), difference() 등등
set_a = {1, 2, 3}
set_b = {1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5}
print(set_b)

# 중복값 제거 활용 방법
#  : a List의 중복값을 제거
a = ["A", "A", "B", "B", "C", "C", "D", "E"]  # List type
# List -> Set(중복값 제거) -> List
# a = set(a)        # ()안의 값을 set type으로 변환
# a = list(set(a))  # ()안의 값을 list type으로 변환
print(a)
print(type(a))

# 4. 딕트(dict)  ex: 복주머니
#  - 순서가 없음(인덱스 없음, 정렬 불가능)
#  - {key : value} 사용 -> key, value 1 pair
#  - key는 중복 불가, value 중복 가능
#  - key를 통해서만 value에 접근 가능
#  - 멤버함수: update(), get(), keys(), values(), items()

# 외부에서 데이터를 받아올 때 대부분 JSON 형식으로 전달
#  - JSON == DICT(동일)

# {"id": "ccw1104", "pw": "abc1234!", "name": "신현우"}

dict_a = {"korea": "Seoul",
          "Canada": "Ottawa",
          "USA": "Washington D.C"}
print(dict_a)
import pprint
pprint.pprint(dict_a)

# update() : dict와 dict 병합
a = {"a": 1,
     "b": 2}
b = {"b": 3,
     "c": 5}
a.update(b)  # 병합시 중복key 있는 경우 입력값(b)이 우선
print(a)

# pop() : dict 원소를 key를 통해서 삭제
c = a.pop("a")
print(a)
print(c)

# in() : ()안의 key값이 존재 확인
print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션[index or key] ex: a[2]
# print(a["f"])    # key가 없으면 error 발생
print(a.get("f"))  # key가 없으면 None 출력(Error X)

# keys(), values(), items()
print(a.keys())    # key만 추출
print(a.values())  # value만 추출
print(a.items())   # (key, value) 추출

print(list(a.keys()))  # 활용 방법

# clear() : dict 초기화
print(a)
a.clear()
print(a)

e = {}
print(type(e))

# 함수 정의
#  1.기본 함수 문법
# def 함수명(parameter1, parameter2, ...):
#     실행문
#     return 반환값

#  2.함수 정의시 "def" 키워드 사용(define)
#  3.인자(argument or parameter) 정의: 함수 입력 값
#  4.return: 함수 종료 의미
#  5.return 반환값: 함수 종료 + 호출문으로 반환값 전달(tuple)
#  6.return 생략가능 -> 들여쓰기 종료되면 함수 종료
#  7.parameter와 return은 사용하지 않을수도 있음
#    (입력과 반환이 없는 함수도 존재)

# 1. 함수 정의

def sub_two_value(x, y):
    n = x - y
    print(f"결과: {n}")
    return n

#  2. 함수 호출

#  * 함수 호출문을 실행하면 함수가 종료되고 호출했던 곳으로 돌아옴
#  - 돌아올 때 반환값이 있으면 호출문 = 반환값
#  - 돌아올 때 반환값이 없으면 호출문 = None
num = sub_two_value(5, 8)
print(num)


# 이름과 나이를 출력하는 함수

def print_info(name, age):
    print(f"이름: {name}, 나이: {age}")


name = input("이름: ")
age = int(input("나이: "))
print_info(name, age)

# return
#  - 기본적으로 함수 종료 의미
#  - return 반환값: 함수 호출문으로 값 전달(tuple type)
#  - return만 사용하면 함수 호출문으로 None 값 전달
#  - return이 없는 경우 들여쓰기 종료되면 함수 종료로 간주
#  - return문 뒤에 오는 코드들은 실행 안됨(Errror X)

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

# 변수의 범위
#  - 변수가 참조 가능한 코드상의 범위를 명서
#  - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
#  - 특정 코드블럭 안에서 선언된 변수를 지역변수
#  - 반대로 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 전역 변수
#  - 같은 이름의 지역변수, 전역변수 존재하는 경우 가까운(지역변수)가 우선순위가 더 높음

num1 = 10  # 전역 변수
num2 = 20  # 전역 변수

# 함수 내에서 함수 밖의 전역변수를 변경하고 싶은 경우?
#  1.return 반환값
a = 1  # 전역
print(a)  # 1 출력

def var_test(a):
    a = a+1  # 지역
    return a
a = var_test(3)
print(a)

# 2. global 키워드를 사용하는 방법(권장 X, 사용금지)
a = 1
print(a)

def var_test():
    global a
    a = a + 1
var_test()
print(a)

# Variable length parameter(가변 길이 인자)
#  - 인자(parameter): 함수 입력값
#  - 함수 입력값의 갯수가 함수를 호출할 때마다 매번 다른 경우
#   -> 가변 길이 인자를 사용해야 함!!!

#  ex) format(), print()
#      print("Hi") print("Hi", "Hello")
# 1.tuple type: *args

# 라이브러리(Library), 패키지(Package), 모듈(Module)
#  - 라이브러리 >= 패지키 >= 모듈

#  1.라이브러리: 여러 패키지와 모듈의 묶음
#  2.패키지: 특정 기능과 관련된 여러 모듈의 묶음
#  3.모듈: 이미 작성된 프로그램(일반적으로 한 파일을 의미)

#  ** 모듈의 종류
#   1.내부 모듈: 파이썬 설치 하면 기본적으로 제공
#   2.외부 모듈: 다른 개발자가 개발 해놓은 모듈
#   3.사용자 정의 모듈: 직접 개발해서 사용하는 모듈

#  ** 모듈 사용 방법
#   - 라이브러리 또는 모듈을 사용하기 위해서는 "import" 필요!

#   가정: requests 내에 1,000개 모듈
#   1.import
#    ex) import requests
#     →  "requqests" 라이브러리 전체 호출(1,000개)
#     →  requests.get()

#   2.from ~ import
#    ex) from requests import get, put, ...
#     →  "requests" 라이브러리 내에서 "get" 모듈만 호출(1,000개 중에 1개)
#     →  get()

#   3.as(Alias:별명)
#    ex) import requests as req
#     →  "requests" 모듈 전체 호출, 그리고 "req"라는 별명 붙이기
#     →  req.get()

# 예외 처리
#  ** 예외(Exception)
#   - 프로그램을 개발하면서 예상하지 못한 상황
#     ex) 사용자의 입력 오류
#   - 예외처리를 사용하면 프로그램이 종료되지 않음
#     프로그램 -> 입력 오류 -> 프로그램 종료(Error)
#     프로그램 -> 입력 오류 -> 예외 처리 -> 프로그램 종료 X
#   - 데이터베이스 또는 파일시스템 사용할 때는 반드시 예외처리!!

#  ** 예외 종류
#   1. 예측 가능한 예외
#     - 발생 여부를 개발자가 사전에 인지 가능 -> 예외 처리
#   2. 예측 불가능한 예외
#     - 서버에서 데이터 받기(서버 화재 발생으로 서버 종료)
#     ex) 스마트폰(카카오톡) -> 00친구와 톡방 -> 카카오 서버 접근 -> 데이터 전달 -> 스마트폰 출력

#  ** 예외 기본문법
# try:
#   예외 발생 가능 코드
# except 예외 타입:
#   예외 발생시 실행되는 코드
# else:
#   예외가 발생하지 않았을 때 실행되는 코드
# finally:
#   예외에 상관없이 무조건 실행(자원 해제)

# 가정: 수강신청 -> 종합정보시스템(조대 서버): 최대 2000명 동시접속
#  - 학생1 컴퓨터 -> 수강신청 -> 종합정보시스템(Connect)
#    수강신청 완료 -> 자원해제(Connect 끊기)

# 정상실행: try -> else -> finally
# 예외실행: try -> except -> finally
# * else, finally 생략 가능
# * try~except 한 쌍

from urllib.request import urlopen, HTTPError

try:
    html = urlopen("http://www.naver.commmmm")
except HTTPError as e:
    print(e)
else:
    print("no error")
finally:
    print("자원해제")

# WebCrawling(웹 크롤링)
#  - 웹 페이지에서 원하는 데이터를 수집하는 기술
#  - 데이터가 필요한 작업 → 원하는 데이터가 없는 경우!
#                           (제공X, 다운X)
#    → 웹크롤링을 사용해서 직접 데이터를 수집

#  - 직업: 웹 크롤러(전문),
#  -       데이터엔지니어(웹크롤링 + @)
#  - 웹크롤링 + 스케줄링 -> 자동화

# 외부 라이브러리(다운로드 + import)
#  1.BeautifulSoup4(bs4)
#  2.Requests
#  3.Selenium

#  웹 페이지
#    - 정적 페이지(Requests + bs4)
#    - 동적 페이지(Selenium + bs4)

# Anaconda Prompt
#  > conda env list -> basic 확인
#  > 없으면: conda create -n basic python=3.8
#  > conda activate basic
#  > pip install requests
#  > pip install beautifulsoup4
#  > pip install selenium
# import requests
# import selenium
# from bs4 import BeautifulSoup

# 웹 프로그래밍 기초(속성)
#  - 프론트 엔드: 사용자 화면 개발
#  - 백 엔드: 서비스와 DB 개발
#  - 풀 스택: 프론트 엔드 + 백 엔드

# MVC 패턴
#  - VIEW(사용자 화면)
#  - CONTROLLER
#  - MODEL(데이터베이스:저장)

# 웹 페이지 화면 구현
#  - 웹 표준: HTML, CSS, Javascript
#  1.HTML: 프레임 구현
#  2.CSS: 디자인(색상, 크기, 모양, 등등)
#  3.Javascript: 동적 기능

# HTML 속성
#  - <tag></tag> 구현
#  - tag 종류: div, span, a, h4, etc...
#  - tag 종속관계
#    <div>
#      <span>
#        <span></span>
#      </span>
#      <span></span>
#    </div>
#    div: 부모
#     ㄴ span: 자식
#    종속관계: 부모자식 (div > span: div태그의 자식 태그인 span)
#              자손(div span: div태그 안에 있는 모든 span)

#  선택자
#   1.ID(#): 유일한 선택자
#   2.CLASS(.): 복수 선택자

import requests
from bs4 import BeautifulSoup
url = "https://v.daum.net/v/20231101111111618"  # 수집하고 싶은 웹사이트 주소

# 1.URL에 접속해서 전체 소스코드 가져오기!
result = requests.get(url)
# status_code: 200(성공)
#              400번대, 500번대 오류
# print(result)
# print(result.text)

# 2.전체소스코드(requests) → bs4
doc = BeautifulSoup(result.text, "html.parser")

# 3.원하는 정보 수집
reg_date = doc.select("span.num_date")[0].get_text()
print(f"날짜: {reg_date}")

title = doc.select("h3.tit_view")[0].get_text()
# select() → 결과: List Type
print(f"제목: {title}")

# 경고: Tag 이름으로는 절대 수집 X
content_list = doc.select("div.article_view p")
# content_list = ["<p>본문1</p>", "<p>본문2</p>",
#                 "<p>본문3</p>", "<p>본문4</p>", ...]

content = ""
# ex) p = "<p>본문1</p>"
for p in content_list:       #        content = content + p.get_text()
    content += p.get_text()  # 반복1: content = "" + "본문1"
print(f"본문: {content}")    # 반복2: content = "본문1" + "본문2"
                             # 반복2: content = "본문1본문2" + "본문3"

from selenium import webdriver

# Chrome 드라이버 경로 설정 (다운로드한 드라이버의 경로를 지정)
chrome_driver_path = "/path/to/chromedriver"

# Chrome 브라우저 열기
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 웹 페이지로 이동
driver.get("https://www.example.com")

# 웹 페이지에서 작업 수행 (예: 요소 찾기, 클릭 등)
# 예제: 페이지 타이틀 출력
print("페이지 타이틀:", driver.title)

# 브라우저 닫기
driver.quit()