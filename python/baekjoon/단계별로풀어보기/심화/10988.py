### 펠린드롬인지 확인하기

# 첫 풀이
"""
ans = 1로 초기화하고 단어의 중간까지 같은지 확인하고 틀리면 0으로 바꾸는 방식
-> 따라서, 틀리면 break로 바로 종료
"""
s = input()
ans = 1


for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        ans = 1
    else:
        ans = 0
        break

print(ans)


# 두 번째 풀이
"""
s == s[::-1] 이면 펠린드롬이므로 1, 아니면 0
-> 따라서, 펠린드롬인지 확인하는 방식
"""
s = input()
print(1 if s == s[::-1] else 0)
