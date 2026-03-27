#### 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())
    
if a+b+c == 180:
    if a == 60 and b ==60:
        print("Equilateral")
    elif a != b and b!=c and c!=a:
        print("Scalene")
    else:
        print("Isosceles")

else:
    print("Error")