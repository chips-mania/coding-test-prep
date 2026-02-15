# 문자열 반복

# 첫 풀이이
num = int(input())
for _ in range(num):
    R, S = input().split()
    R = int(R)
    for ch in S:
        print(ch*R, end = "")
"""
틀린 이유는 테스트 케이스 간 줄바꿈이 없어서.
-> 따라서, 테스트 케이스 간 줄바꿈을 추가하기 위해 print()를 사용해야 함.
"""

# 수정 후 풀이
num = int(input())
for _ in range(num):
    R, S = input().split()
    R = int(R)
    for ch in S:
        print(ch*R, end = "")
    print()


# 좀 더 파이써닉한 코드

T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    print(''.join(R*ch for ch in S))

"""
T는 테스트 케이스의 개수
R은 반복 횟수
S는 문자열

join() 메서드는 리스트의 모든 요소를 하나의 문자열로 결합하는 메서드
-> R*ch for ch in S 는 문자열 S의 각 문자를 R번 반복한 문자열을 리스트로 만듦
-> ''.join(R*ch for ch in S) 는 리스트의 모든 요소를 하나의 문자열로 결합
-> 따라서, 문자열 S의 각 문자를 R번 반복한 문자열을 출력

join() 메서드를 사용하는 것이 좋은 이유
-> print는 문자열은 immutable이므로, 문자열을 계속 변경하면 새로운 문자열 객체를 생성하게 됨
-> 따라서, join() 메서드는 누적 문자열을 계속 새로 만들지 않는다는 장점이 있음
-> 따라서, join() 메서드가 더 효율적
"""