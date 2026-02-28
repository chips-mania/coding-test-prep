#### 분수찾기

### 첫 풀이
"""
1. 입력받은 수가 어느 layer에 위치하는지 찾기
2. 짝수 layer인지, 홀수 layer인지 판별하여 분모, 분자 초기화
3. layer내에서 몇번 이동해야하는지 계산
4. 분모 분자 갱신

# 개선점
1. layer 내 X번째 수의 위치를 구하면 for문으로 분모, 분자 갱신이 필요없음
2. 분모 분자의 초기값 설정 시 가독성 떨어짐 -> 개선 필요

"""
X = int(input())

# layer
layer = 1

# 층 누적
N = 1

# 몇번째 layer인지 찾기
while X > N:            
    layer += 1
    N += layer

# 분모, 분자 초기화
if layer%2==0:
    n = 0
    d = layer+1
else:
    n = layer+1
    d = 0

# X가 2면 한번, X가 3이면 두번 반복 
# X가 4면 N은 6 
for _ in range(layer-(N-X)):
    # layer가 홀짝인 두 경우로 나누기
    # layer가 짝수면
    if layer%2==0:
        n+=1
        d-=1

    else:
        n-=1
        d+=1

print(n,"/",d, sep="")
    

### 정답 풀이
"""
[분수 찾기 핵심 아이디어]
1. X가 어느 대각선(layer)에 속하는지 찾는다. (삼각수 누적)
2. 해당 layer의 시작 번호(start)와, layer 내 위치(k, 1-based)를 구한다.
3. layer의 홀/짝에 따라 분자/분모가 증가/감소 방향이 달라진다.
   - 짝수 layer: 1/layer -> layer/1
   - 홀수 layer: layer/1 -> 1/layer

"""

X = int(input())

layer = 1
N = 1

# 여기가진 동일
while X > N:
    layer += 1
    N += layer

# X가 존재하는 layer의 시작 위치를 start로 초기화
start = N - layer + 1      # 이 layer의 시작 X
# X가 존재하는 layer에서 X의 위치를 k로 초기화
k = X - start + 1          # 이 layer에서 X의 위치(1부터)

# for문없이 분모, 분자 바로 구하기
if layer % 2 == 0:         # 짝수 layer: 1/layer -> layer/1
    n = k
    d = layer - k + 1
else:                      # 홀수 layer: layer/1 -> 1/layer
    n = layer - k + 1
    d = k


# f-string 사용하여 출력
print(f"{n}/{d}")