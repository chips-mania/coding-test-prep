#### 색종이
### 첫 풀이
"""
아이디어는 총 색종이 넓이에서 겹친 사각형 넓이를 빼는 것
-> 이 경우 종이가 세 장 이상 한번에 겹치는 경우에서 에러가 발생
-> 세장이 겹쳐있으니 총 넓이에서 두번 빼야함 하지만 겹치는 이벤트가 세번 발생하므로 세번 빼게되어서 틀림
"""
n = int(input())

# 각 색종이 좌측하단 좌표
p = []
for i in range(n):
    # 예제 1: p = [[3,7], [15,7], [5,2]]
    p.append(list(map(int,input().split())))

#
# 겹친 사각형 넓이
extent = n*100
for i in range(n-1):
    for j in range(1, n-i):
        # 겹친 사각형 좌표
        # overlap_cordinate = []
        if abs(float(p[i][0]) - float(p[i+j][0])) < 10 and abs(float(p[i][1]) - float(p[i+j][1])) < 10:
            a = max(p[i][0], p[i+j][0])
            b = min(p[i][0]+10, p[i+j][0]+10)
            c = max(p[i][1], p[i+j][1])
            d = min(p[i][1]+10, p[i+j][1]+10)
            # print(a, b, c, d)
            extent -= (b-a)*(d-c)
        
print(extent)


### 수정 후 풀이
n = int(input())

# 도화지는 가로 세로 크기가 100 -> 0부터 100까지 101칸
paper = [[0]*101 for _ in range(101)]

# 칸을 채우면 됨
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1
            
ans =sum(sum(row) for row in paper)
print(ans)