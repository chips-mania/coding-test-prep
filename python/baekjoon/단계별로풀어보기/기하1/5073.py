####삼각형과 세변
while True:
    a,b,c = map(int, input().split())
    len_list = [a,b,c]
    
    if a == b == c == 0:
        break

    elif 2*max(len_list) < sum(len_list):
        if a == b == c:
            print("Equilateral")
        elif a != b and b != c  and a !=c:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")

