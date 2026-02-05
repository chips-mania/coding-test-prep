# 문자열

"""
문제
문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.

출력
각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.


예제 입력 1 
3
ACDKJFOWIEGHE
O
AB

예제 출력 1 
AE
OO
AB

"""

word_num = int(input())

for i in range(word_num):
    word = input()
    print(word[0]+word[len(word)-1])


"""
좀 더 파이써닉한 코드 
-> strip()은 문자열 양쪽의 공백을 제거하는 메서드
-> strip() 넣는 이유: 입력에 개행(줄바꿈문자, \n)/공백 섞여도 안전
-> 그래서 문자 입력 받으면 거의 습관처럼 strip() 넣음

word_num = int(input())

for _ in range(word_num):
    word = input().strip()
    print(word[0]+word[-1])

"""