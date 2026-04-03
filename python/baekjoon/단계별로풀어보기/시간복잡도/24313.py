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
### 정답
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