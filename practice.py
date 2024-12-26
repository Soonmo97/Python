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


# - 슬라이싱
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

# 방법 4 (v3.6 이상~) f"" 변수 사용
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
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 (추가)
print(cabinet)
cabinet["A-3"] = "김종국" # "A-3"  키 값이 존재해서 덮어쓰기
cabinet["C-20"] = "조세호" # "C-20" 키 값이 없기에 추가
print(cabinet)

# 간 손님 (삭제) del
del cabinet["A-3"]
print(cabinet)

# key 들만 출력 keys()
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력 values()
print(cabinet.values()) # dict_values(['김태호', '조세호'])
 
# key, value 쌍으로 출력 items() 
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점 (모두 삭제) clear()
cabinet.clear()
print(cabinet) # {}



