a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

l_1 = [a,c,e]
l_2 = [b,d,f]
l_3=[]
for i in l_1:
    if l_1.count(i)%2 == 1:
        l_3.append(i)
for i in l_2:
    if l_2.count(i)%2 == 1:
        l_3.append(i)
        
print(*l_3)