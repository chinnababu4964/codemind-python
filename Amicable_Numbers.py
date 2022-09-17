m=int(input())
n=int(input())
sum1=0
sum2=0
for i in range(1,m):
    if m%i==0:
        sum1+=i
for j in range(1,n):
    if n%j==0:
        sum2+=j
if m==sum2 and n==sum1:
    print("Amicable")
else:
    print("Not Amicable")