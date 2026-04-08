a,b,c,d,e,f = map(int, input().split())
x = ((c/a)-(f/d))/((b/a)-(e/d))
y = (c - (a*x))/b

print(x,y)