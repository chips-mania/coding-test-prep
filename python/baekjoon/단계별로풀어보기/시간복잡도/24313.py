#### 알고리즘 수업 - 점근적 표기 1
"""
c는 fn_1+1이어야 함

예제1
7n+7 <= 8n

7 <= n
이때, n_0는 7이됨

만약 
7n +7 <= 9n으로 주어진 경우

3.5 <= n이므로 n_0 = 4

"""
# fn_1, fn_2 = map(int, input().split())


# c = int(input())
# n_0 = int(input())


# ### 첫 풀이
# # import math

# # if c >= fn_1+1 and math.ceil(fn_2/(c-fn_1)) == n_0:
# #     print(1)
# # else:
# #     print(0)

# if c == fn_1+1 and fn_2 == n_0:
#     print(1)
# else:
#     print(0)
    
##############################################
### 두번째 풀이
import math

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 반드시 c는 a1보다는 커야함
if c <=a1:
    print(0)
    
# 그 중 수식을 만족하면 ok
elif n0 >= math.ceil(a0/(c-a1)):
    print(1)
    
# 그외는 0을 출력
else:
    print(0)


### 정답풀이 -> a0가 음수일 경우 고려
# 입력
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 게수 확인
# a1*n + a0 <= c*n 을 만족해야 1이므로 그 외는 0을 출력력
if a1 > c:
    print(0)

# 위 수식을 모든 n에 대해 만족해야하는데 n0만 만족하면 전체 n에 대해 만족 
# 그 이유는 앞서 조건문에서 걸렀으므로 a1 <= c을 만족
# a0 <= (c - a1)*n 이라는 식에서 (c - a1)이 양수이므로 n이 커질수록 a0도 커짐
# 따라서 n의 최솟값인 n0에서만 만족하면 전체 n에 대해 만족
elif a1 * n0 + a0 <= c * n0:
    print(1)
else:
    print(0)