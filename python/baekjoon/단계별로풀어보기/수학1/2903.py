#### 중앙 이동 알고리즘

### 첫 풀이

# 9 - 25 - 81 - ...
N = int(input())

# 한 변의 점 개수
p = 2

for i in range(N):
    p = 2*p-1
    
print(p**2)