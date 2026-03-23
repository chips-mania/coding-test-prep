#### 직사각형에서 탈출

### 첫 풀이

x,y,w,h = map(int, input().split())
# print(x,y,w,h )

print(min(x,y,w-x, h-y))