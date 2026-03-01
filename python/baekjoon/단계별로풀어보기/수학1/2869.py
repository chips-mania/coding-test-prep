# #### 달팽이는 올라가고싶다

### 첫 풀이
"""
시간초과 나는 풀이

"""
# A, B, V = map(int, input().split())
# days = 0
# distance = 0
# while distance < V:
#     distance = distance + A
#     if distance >= V:
#         days += 1
#         break
        
#     else: 
#         distance = distance - B
#         days += 1

# print(days)



### 두번째 풀이
"""
올라가는 길이랑 내려가는 길이를 빼면 이동거리
이동거리와 날을 곱하고 거기에 올라가는 길이를 더해서 전체 길이가 넘기만 하면됨

맞추긴했지만 직관적이지는 않음 
-> +1을 해주는 이유는 마지막 날 올라가는 거리를 고려하기 위함인데, 안쓰는 풀이가 존재
-> 또한, ceil을 사용하는 이유는 소수점 이하의 날짜를 올림하기 위함인데, 정수만으로 계산하는 풀이가 존재
"""
import math
A, B, V = map(int, input().split())
move = A-B
day = (V-A)/move
print(math.ceil(day)+1)

### +1을 해주지 않는 풀이
import math
A, B, V = map(int, input().split())
print(math.ceil(V-B)/(A-B))


### ceil을 사용하지 않는 풀이
"""
ceil은 올림인데, +1한 몫이 나오도록 더해준 후 몫을 구하면 ceil을 사용하지 않은 것과 동일한 결과를 얻을 수 있음
자주 사용하는 공식이므로 외우기!
"""
A, B, V = map(int, input().split())
a = V-B
b = A-B
print((a+b-1)//b)