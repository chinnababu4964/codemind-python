def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    while n:
        if prime(n%10)!=True:
            print("Not Mega Prime")
            break
        n=n//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")