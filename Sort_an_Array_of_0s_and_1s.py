n=int(input())
b=list(map(int,input().split()))
z=b.count(0)
o=b.count(1)
ss=[]
for i in range(z):
    ss.append(0)
for j in range(o):
    ss.append(1)
print(*ss)