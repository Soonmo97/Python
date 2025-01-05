# - 숫자 자료형
# print(5)
# print(2*8)
# print(3 * (3+1))


# - 문자 자료형
# print('풍선')
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ" * 9)


# - 참 / 거짓
# print(5>10)
# print(10>5)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))

# 애완동물을 소개해 주세요~ (변수), 
# 정수형, 불린은 str로 문자열 변환 필수
# 단 +가 아닌 ,로 사용하면 변환하지 않아도 됌 대신 , 는
# 한칸 띄어쓰기가 적용된다
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# # print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 " , age , "살이며, " , hobby , "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장: XX 행 열차가 들어오고 있습니다.
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")


# - 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 19
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5/3) # 1.666666.. 소수점까지(실수 float형)
# print(5//3) # 몫 1
# print(10//3) # 3

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3 == 3) # True
# print(4 == 2) # False
# print(3 + 4 == 7) # True
# print(1 != 3) # True
# print(not(1 != 3)) # False

# print((3 > 0) and (3 < 5)) # True AND 연산자
# print((3 > 0) & (3 < 5)) # True 

# print((3 > 0) or (3 > 5)) # True OR 연산자
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) # True 모두 참이기 때문에
# print(5 > 4 > 7) # False (4 > 7) 이 거짓이기 떄문에 False


# - 간단한 수식
# number = 2 + 3 * 4 # 14
# number += 2 # number = number +2 16
# print(number) # 16
# number -= 2 # 14
# number *= 2 # 28
# number %= 2 # 0
# print(number)
# number += 3+4 # 7
# number /= 2 # 3.5
# number //= 2 # 1.0
# print(number)


# - 숫자처리함수
# 절대값 구하기 abs()
# print(abs(-5)) # 5
# 제곱 pow
# print(pow(4, 2)) # 4 ^ 2 = 4 * 4 = 16
# 최대값 최소값 max, min
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5 
# 반올림
# print(round(3.14))# 3
# print(round(4.99)) # 5


# - math 라이브러리 함수
# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) # 제곱근. 4


# - Random 함수
# from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성

# 로또 번호 뽑기 random = radrange = randint
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성 (범위 지정)
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 a, b도 포함

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1 ~ 3일은 스터디 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
# from random import *

# date = randrange(4, 29)
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")


# - 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentece3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentece3)


# - 문자열 슬라이싱
# jumin = "990120-1234567"

# print("성별: " + jumin[7]) # 인덱스는 0부터, 7번째를 가져옴
# print("연: " + jumin[0:2]) # 0 ~ 2 직전까지 (0, 1) 
# print("월: " + jumin[2:4]) # (2,3)
# print("일: " + jumin[4:6])

# print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지 (0 1 2 3 4 5)
# print("뒤 7자리: " + jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리 (뒤에부터): " + jumin[-7:]) # 맨 뒤(-1)에서 7번째부터 끝까지


# - 문자열 처리함수
# python = "Python is Amazing"
# print(python.lower()) # lower() 모든 문자 소문자로 변환
# print(python.upper()) # upper() 모든 문자 대문자로 변환
# print(python[0].isupper()) # 첫번째 값이 대문자인지 확인 False
# print(len(python)) # len() 문자열 길이 반환 17
# print(python.replace("Python", "Java")) # replace("찾는 문자", "바꿀 문자") 문자 바꾸기

# index = python.index("n") # index() 인덱스 위치 값 찾기
# print(index) # 5
# index = python.index("n", index + 1) # 첫 번째 위치에 +1 인덱스부터 다음 "n" 위치
# print(index) # 15

# print(python.find("Java")) # find() 인덱스 위치 값 찾기
# # 단, find()는 없는 값을 입력 시 -1 반환

# # print(python.index("Java")) # index()는 없는 값을 입력 시 에러 발생 후 종료
# print(python.count("n")) # count() 존재하는 문자 개수 반환 2


# - 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1  % 
# print("나는 %d살입니다." % 20) # %d = % 정수
# print("나는 %s를 좋아해요." % "파이썬") # %s = % 문자열
# print("Apple 은 %c로 시작해요." % "A") # %c = % 문자 하나 (Character)
# %s 로 출력하면 문자열이 아닌 다른 자료형(ex- 정수형)을 넣어도 에러 안생김
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러개 입력

# 방법 2  format() 
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간")) # 숫자로 format() 안의 문자열 순서 지정
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간")) # 빨간(1) 파란(0) 순으로 출력

# 방법 3  format() 변수 사용
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))

# 방법 4 f-string (v3.6 이상~) f"" 변수 사용
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


# - 탈출 문자
# print("백문이 불어일견\n백견이 불여일타") # \n 줄바꿈

# 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.") # \" 따옴표 출력을 위한 \
# print("저는 \'나도코딩\'입니다.") # \' 작은따옴표 출력을 위한 \

# \\ : 문장 내에서 \
# print("C:\\Users\\ksunm\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple") # RedApple

# \t : 탭
# print("Red\tApple") # Red     Apple

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 = 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                   (nav)             (5)           (1)             (!)

# 예) 생성된 비밀번호 : nav51!
# url = "http://naver.com"
# url = "http://youtube.com"
# pw = url.replace("http://", "") # 규칙 1  -> naver.com
# pw = pw[:pw.index(".")] # pw[0:5] -> 0 ~ 5 직전까지. (0 1 2 3 4) -> naver
# pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
# # print("{0} 의 비밀번호는 {1} 입니다.".format(url, pw))
# print(f"{url} 의 비밀번호는 {pw} 입니다.")


# - 리스트 [] : 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # append() 맨 뒤에 추가
# # 하하씨가 다음 정류장에서 다음 칸에 탐 
# subway.append("하하")
# print(subway)

# insert() 추가할 인덱스 위치, 추가될 값
# 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# pop() 맨 뒤에 빼기
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) 
# print(subway)

# print(subway.pop()) 
# print(subway)

# print(subway.pop()) 
# print(subway)

# count() 개수 확인
# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# sort() 정렬
# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list) # [1, 2, 3, 4, 5]

# reverse()
# 순서 뒤집기 가능
# num_list.reverse()
# print(num_list) # [5, 4, 3, 2, 1]

# clear()
# 모두 지우기
# num_list.clear()
# print(num_list) # []

# 다양한 자료형 함께 사용 가능
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# # print(mix_list) # ['조세호', 20, True]

# # extend() 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# - 사전(Dictionary) (key 정렬, 중복 허용 x) 키: 값 형태
# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # [] 방식은 입력한 키가 존재하지 않을 때 에러발생
# print(cabinet.get(5)) # get() 방식은 입력한 키가 존재하지 않을 때 None
# print(cabinet.get(5, "사용 가능")) # 키 값이 없으면 "사용 가능"
# print("hi")

# in 존재여부 key in Dictionary명 (True, False)
# print(3 in cabinet) # True
# print(5 in cabinet) # False

# key 값은 정수형이 아니여도 가능
# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님 (추가)
# print(cabinet)
# cabinet["A-3"] = "김종국" # "A-3"  키 값이 존재해서 덮어쓰기
# cabinet["C-20"] = "조세호" # "C-20" 키 값이 없기에 추가
# print(cabinet)

# # 간 손님 (삭제) del
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력 keys()
# print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# # value 들만 출력 values()
# print(cabinet.values()) # dict_values(['김태호', '조세호'])
 
# # key, value 쌍으로 출력 items() 
# print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# # 목욕탕 폐점 (모두 삭제) clear()
# cabinet.clear()
# print(cabinet) # {}


# - 튜플 : 리스트와 다르게 내용 변경 및 추가 불가능, 속도가 리스트보다 빠름, 변경되지 않는 목록에 사용
# menu = ("돈까스", "치즈까스") # ()
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") # Error

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩") # Tuple Unpacking, 변수 선언과 동시에 할당이 이루어짐
# print(name, age, hobby)


# - 집합 (Set) : 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set) # {1, 2, 3}

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"]) # list로 생성 후 set()으로 감싸기 가능

# # 교집합 : &, intersection() (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 : |, union() (java 도 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 : -, difference() (java 를 할 수 잇지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # 추가 : add() (python 할 줄 아는 사람이 늘어남)
# python.add("김태호")
# print(python)

# # 삭제 : remove() (java 를 잊었어요)
# java.remove("김태호")
# print(java)


# - 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # set

# menu = list(menu) # set -> list로 변환
# print(menu, type(menu)) # list

# menu = tuple(menu) # list -> tuple
# print(menu, type(menu)) # tuple

# menu = set(menu) # typle -> set
# print(menu, type(menu)) # tuple

# Dictionary 는 key(), values(), items()를 사용해야함
# menu2 = {"커피": 3000, "우유": 1000, "주스": 2000}
# print(menu2, type(menu2)) # dict

# menu2 = list(menu2.items()) # dict_items -> list
# print(menu2, type(menu2)) # list

# menu2 = set(menu2.values()) # dict_values -> set
# print(menu2, type(menu2)) # set

# menu2 = tuple(menu2.keys()) # dict_values -> tuple
# print(menu2, type(menu2)) # tuple


# Quiz 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# # print(lst)
# # shuffle(lst) # shuffle() 무작위로 섞기
# # print(lst)
# print(sample(lst, 1)) # sample() 무작위로 뽑기 1은 개수 
# 단, shuffle, sameple 은 순서가 있는 list, tuple, 문자열 등을 사용하거나
# set 을 사용하려면 sorted(set)으로 정렬해야함.

# 나의 풀이
# from random import *
# # id 리스트
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# # print(type(users))
# users = list(users)
# # print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
# print(winners)

# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print("-- 축하합니다 --")


# - if
# weather = input("오늘 날씨는 어떄요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# - for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for wating_no in [0, 1, 2, 3, 4]:
#     print(f"대기번호 : {wating_no}")

# for wating_no in range(1, 6): # 1, 2, 3, 4, 5
#     print(f"대기번호 : {wating_no}")

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print(f"{customer}, 커피가 준비되었습니다.")


# - while
# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}, 커피가 준비되었습니다. {index}")
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.") 

# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 커피가 준비되었습니다. 호출 {index} 회")
#     index += 1

# 문자열, input()으로 제어
# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print(f"{customer}, 커피가 준비되었습니다.")
#     person = input("이름이 어떻게 되세요? ")


# - continue 와 break (생략과 종료)
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1 ~ 10
#     if student in absent: # in list
#         continue
#     elif student in no_book:
#         print(f"오늘 수업 여기까지, {student}는 교무실로 따라와")
#         break
#     print(f"{student}, 책을 읽어봐")


# - 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# # i 는 리스트에 있는 요소들, i+100값을 리스트에 저장
# print(students) # [101, 102, 103, 104, 105]

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5, 51) # 5 ~ 50 분 소요시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
#         print(f"[O] {i}번째 손님 (소요시간 : {time}분 ")
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print(f"[ ] {i}번째 손님 (소요시간 : {time}분 ")

# print(f"총 탑승 승객 : {cnt} 분")


# - 함수
# 선언 def 함수명():
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()


# - 전달값과 반환값
# def deposit(balance, money): # 입금 balance: 잔액, money: 입금된 금액
#     print(f"입금이 완료되었습니다. 잔액은 {balance + money} 원입니다.")
#     return balance + money

# def withdraw(balance, money) : # 출금
#     if balance >= money: # 잔액이 출금액보다 같거나 많으면
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money} 원입니다.")
#         return balance - money
#     else: 
#         print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원입니다.")
#         return balance
    
# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission # 여러개 값 반환 가능

    
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print(f"수수료 {commission} 원이며, 잔액은 {balance} 원입니다.")


# - 기본값
# def profile(name, age, main_lang): 
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"): 
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

# profile("유재석")
# profile("김태호")


# - 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="파이썬", age=25, name="김태호")


# - 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t", end=" ") # end=" " 다음 문장 줄바꿈 없이 이어서
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language): # 서로 다른 개수의 값을 넣어줄 때 *매개변수 가변인자
# language 는 Tuple 형태로 받아옴
#     print(f"이름 : {name}\t나이 : {age}\t", end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print() # 줄바꿈

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")


# - 지역변수와 전역변수(global)
# 함수 내에서 전역변수 접근은 global
# 가급적 전역변수를 직접 사용하기보다는 매개변수로 넘겨줘서 
# 반환값을 사용하는 것이 좋음
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print(f"[함수 내] 남은 총 : {gun}")

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print(f"[함수 내] 남은 총 : {gun}")
#     return gun

# print(f"전체 총 : {gun}")
# checkpoint(2) # 2명이 경계근무 나감
# gun = checkpoint_ret(gun, 2)
# print(f"남은 총 : {gun}")


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자: 키(m) x 키(m) x 22
#  여자: 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#        * 함수명: std_weight
#        * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")


# - 표준 입출력
# sep="" : 사이에 들어갈 문자 지정
# print("Python", "Java", sep=" vs ") # Python vs Java
# # end="" : 문장의 끝을 바꾸기 (줄바꿈 없어짐)
# print("Python", "Java", end="?") # Python Java?무엇이 더 재밌을까요?
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # stdout 표준출력
# print("Python", "Java", file=sys.stderr) # stderr 표준에러

# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items(): # key와 value가 각각 담김
    # print(subject, score) # 수학 0
                            # 영어 50
                            # 코딩 100
    
    # ljust(8) : 8칸 공간확보 후 왼쪽 정렬
    # rjust(4) : 4칸 공간확보 후 오른쪽 정렬
    # int -> str(int) 필요
    # print(subject.ljust(8), str(score).rjust(4), sep=":") 

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21) : # 1 ~ 20
#     # zfill(3) : 3칸 공간확보 후 채움, 빈 공간은 0으로 채움
#     ex) 대기번호 : 020
#     print("대기번호 : " + str(num).zfill(3))


# input(): 항상 문자열로 저장 (int를 넣어도)
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")


# - 다양한 출력포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #        500

# 양수일 땐 + 로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) #       +500
# print("{0: >+10}".format(-500)) #       -500

# 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500)) # 500______

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000)) # 100,000,000,000

# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000000)) # +100,000,000,000
# print("{0:+,}".format(-100000000000)) # -100,000,000,000

# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(100000000000)) # +100,000,000,000^^^^^^^^^^^^^^

# # 소수점 출력
# print("{0:f}".format(5/3)) # 1.666667

# # 소수점 특정 자리 수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3)) # 1.67


# - 파일입출력
# open() 열기, w: write 생성
# score_file = open("score.txt", "w", encoding="utf-8") # utf-8 한글설정
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close() # 파일 닫기
# score.text 파일이 생김

# "a": append 이어서 쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# score.text 파일에 이어서 작성됨

# "r": read 파일 읽기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read()) # 한 번에 읽어옴
# score_file.close()
# --- 출력결과 ---
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# - Pickle
# 파일에 정보를 저장하고 읽어올 수 있도록 도와주는 라이브러리
# import pickle
# profile_file = open("profile.pickle", "wb") # 인코딩 설정 필요없음
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
# print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
# profile_file.close()


# - With
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# # profile_file.close() 생략. 자동으로 처리

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())


# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# for i in range(1, 51):
#     with open(f"{i}주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(f"- {i} 주차 주간보고 -")
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 :")


# - 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 36

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# 위와 같은 방식으로 작성하면 유닛의 수가 많아질수록 코드가 무수히 길어지기에 클래스 필요

# 클래스 생성, __init__
# __init__ : 생성자, self를 제외한 매개변수와 동일한 개수와 순서로 인자를 전달해야함(기본값 지정 가능)
# self 는 Python 클래스에서 인스턴스 자신을 참조하는 특별한 매개변수.
# self가 필요한 이유:
# 인스턴스 변수 접근 - 클래스 내부에서 객체 고유의 데이터를 저장하거나 변경하려면 self를 통해 인스턴스 변수에 접근해야 한다.
# 다른 메서드 호출 - 클래스 내부에서 다른 메서드를 호출할 때도 self를 사용해야 한다.

class Unit:
    def __init__ (self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력{self.damage}")

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)


# - 멤버변수

# 레이스: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}")

# # 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗긴 레이스", 80, 5)
# wraith2.clocking = True # 클래스 외부에서 변수 확장, 확장한 객체에만 적용 클래스 적용 x
# if wraith2.clocking == True:
#     print(f"{wraith2.name} 는 클로킹 상태입니다.")


# - 메소드

# 공격 유닛
# class AttackUnit:
#     def __init__ (self, name, hp, damage): 
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴되었습니다.")

# # 파이어뱃: 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


