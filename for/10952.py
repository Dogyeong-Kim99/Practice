a=-1
b=-1
while True:
    A,B=input().split()
    a=int(A)
    b=int(B)
    if a==0 and b==0:
        exit()
    print(a+b)
