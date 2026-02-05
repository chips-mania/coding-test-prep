# 아스키 코드
"""
문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.
"""


# 아스키 코드 변환 함수
# ord()는 문자의 아스키 코드 값을 반환하는 함수
# chr()는 아스키 코드 값을 문자로 변환하는 함수

# 입력 문자가 어떤 종류인지 판별하는 방법
# ch.isalpha() -> 문자인지 판별
# ch.isdigit() -> 숫자인지 판별
# ch.isspace() -> 공백인지 판별
# ch.isupper() -> 대문자인지 판별
# ch.islower() -> 소문자인지 판별
# ch.isalnum() -> 문자 또는 숫자인지 판별
# ch.isascii() -> 아스키 코드 값이 0-127 사이인지 판별
# ch.isprintable() -> 출력 가능한 문자인지 판별


# ch = input()
# print(ord(ch))


N = 5
num = "54321"
num_lst = []

for i in range(N):
    num_lst.append(int(num[i]))

print(sum(num_lst))