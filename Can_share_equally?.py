x,y=input().split()
a=int(x)
b=int(y)
c=a+(b*2)
if a==0 and b%2!=0:
    print("NO")
elif c%2==0:
    print("YES")
else:
    print("NO")