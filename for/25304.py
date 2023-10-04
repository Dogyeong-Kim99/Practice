sum=int(input())
N=int(input())
total=0
for i in range(N):
    A,B=input().split()
    a=int(A)
    b=int(B)
    total=total+a*b
if total==sum:
    print("Yes")
else:
    print("No")