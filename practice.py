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
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")