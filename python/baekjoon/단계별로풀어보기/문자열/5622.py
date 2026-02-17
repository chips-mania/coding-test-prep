## 다이얼

# 첫 풀이 
"""
a부터 z까지 알파벳 리스트를 만들고, 
입력받은 문자의 인덱스를 찾아서 
해당 인덱스의 알파벳이 속한 그룹을 찾아서 
시간을 계산하는 방식

-> 풀리긴한데, 너무 코드가 길어서 비효율적임
-> 추가로, if 0 <= idx <= 2:    # abc
이부분에서 범위지정을 실수하는 등 실수하기 쉬운 부분이 있었음
"""
# word = input()

# def solve(a):
#     letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    
#     idx = letters.index(a.lower())

#     if 0 <= idx <= 2:    # abc
#         return 3
#     elif 3 <= idx <= 5:  # def
#         return 4
#     elif 6 <= idx <= 8:  # ghi
#         return 5
#     elif 9 <= idx <= 11: # jkl
#         return 6
#     elif 12 <= idx <= 14:# mno
#         return 7
#     elif 15 <= idx <= 18:# pqrs
#         return 8
#     elif 19 <= idx <= 21:# tuv
#         return 9
#     else:                # wxyz (22~25)
#         return 10

# result = 0

# for i in range(len(word)):
#     result += solve(word[i])
    
# print(result)


################################################################################
# 수정 후 풀이
word = input().strip()

# 다이얼 그룹을 리스트로 만들어놓음
dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# answer 초기화
ans = 0
result = 0

# 입력받은 문자를 하나씩 순회
for ch in word:

    # 다이얼 그룹을 하나씩 순회
    for i in range(len(dials)):

        # 입력받은 문자가 어느 다이얼 그룹에 속하는지 확인
        if ch in dials[i]:

            # i는 다이얼 그룹의 인덱스이므로 3을 더해서 시간을 계산
            ans += i + 3
            break

# 결과 출력
print(ans)