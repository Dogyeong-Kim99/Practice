A,B=input().split()
H=int(A)
M=int(B)
if M>=45:
    M=M-45
    print("%d %d"%(H,M))
else:
    M=60+(M-45)
    if H>0:
        H=H-1
        print("%d %d"%(H,M))
    else:
        print("23 %d"%M)