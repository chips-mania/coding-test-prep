# 숫자의 합


N = 5
num = "54321"
num_lst = []

for i in range(N):
    # num[i]는 문자열이므로 int로 변환
    num_lst.append(int(num[i]))

print(sum(num_lst))


"""
num[i]는 문자열이므로 int로 변환해주어야함

"""