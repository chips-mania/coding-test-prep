#### 진법 변환

### 첫 풀이
"""
1. 입력받은 문자열을 순회하며 알파벳인지 확인
2. 알파벳이면 알파벳에 해당하는 숫자로 변환
3. 숫자와 진법을 곱하여 더함
-> str인지 int인지 확인해서 변환
"""

target, num = input().split()

# ord('A') = 65
convert_dict = {chr(i): i - 55 for i in range(ord('A'), ord('Z')+1)}


ans = 0
for i in range(len(target)):
    t = target[i]
    
    if target[i].isalpha():
        t = convert_dict.get(t)
    ans += int(t)*int(num)**(len(target)-1-i)
print(ans)


### 수정 후 풀이
"""
누적곱방식
현재값 = 현재값 x 진법 + 새 숫자
예제 1을 보면, ZZZZZ 36
-> 자리 별로 계산하면 
(36^4 * 35) + (36^3 * 35) + (36^2 * 35) + (36^1 * 35) + (36^0 * 35)

-> 누적곱 방식으로 계산하면
1번째 Z:
ans = 0×36 + 35 = 35

2번째 Z:
ans = 35×36 + 35 = 1295

3번째 Z:
ans = 1295×36 + 35

4번째 Z:
ans = (이전값)×36 + 35

5번째 Z:
ans = (이전값)×36 + 35
"""
target, base = input().split()
base = int(base)
ans = 0

for ch in target:
    if '0' <= ch <= '9':
        val = ord(ch) - ord('0')
    else:
        val = ord(ch) - ord('A') + 10
    ans = ans * base + val

print(ans)



### 파이써닉한 풀이
"""
파이썬 내장 진법 변환기능
-> int(문자열, 진법)을 사용하면 문자열을 진법으로 변환할 수 있음
-> 예제 1을 보면, ZZZZZ 36
-> int("ZZZZZ", 36) = 183707215

-> 일반적인 사용 : int(문자열) -> 10진법으로 변환
-> 진법 지정 : int(문자열, 진법) -> 진법으로 변환
"""
n, b = input().split()
print(int(n, int(b)))