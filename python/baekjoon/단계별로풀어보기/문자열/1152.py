## 단어의 개수

# 첫 풀이
"""
단어를 하나씩 순회해서 공백의 갯수를 센 다음 +1
-> 문제점은 공백만 있는 경우는 처리가 안됨
-> if else로 나누어서 처리할 수 있음음
"""
S = input().strip()
S = list(S)
cnt = 0

for ch in S:
    if ch==" ":
        cnt += 1

print(cnt+1)


# 정답 코드
"""
split() 메서드는 문자열을 공백을 기준으로 나누어서 리스트로 만드는 메서드
-> 따라서, 단어의 개수는 리스트의 길이(원소의 갯수)와 같음
"""
S = input().strip()
print(len(S.split()))
