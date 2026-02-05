# 평균

# test_num = int(input())
# grades = list(map(int, input().split()))

test_num = 3
grades = [40, 80, 60]


M = max(grades)
proc_grades = []

for i in range(len(grades)):
    proc_grades.append(grades[i]/M*100)

proc_M = sum(proc_grades)/len(proc_grades)
    
print(proc_M)


"""
평균을 구하는 함수
-> avg()를 쓸 수 있지만 내장함수가 아니므로로
sum(proc_grades)/len(proc_grades)로 구현

"""


### 혹은 함수를 직접 만들어서 쓸수도? -> 코드가 길어진다는 단점
# test_num = 3
# grades = [40, 80, 60]


# def avg(grades):
#     M = sum(grades)/len(grades)
#     return M    # 평균 반환

# M = max(grades)
# proc_grades = []

# for i in range(len(grades)):
#     proc_grades.append(grades[i]/M*100)

# proc_M = avg(proc_grades)
    
# print(proc_M)


"""
# 분모 0 예외처리

M =  max(grades)
if M==0:
    print(0.0)
else:
    print(sum(grades * 100 / (len(grades*M))))
"""
