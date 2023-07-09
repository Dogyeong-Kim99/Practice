A,B=input().split()
H=int(A)
M=int(B)
P=int(input())
P_H=P//60
P_M=P%60
H=(H+P_H)%24
if M+P_M>60:
    H=H+1
    if H==24:
        H=0
    M=M+P_M-60
    print("%d %d"%(H,M))
elif M+P_M==60:
    H=H+1
    if H==24:
        H=0
    M=0
    print("%d %d"%(H,M))
else:
    M=M+P_M
    print("%d %d"%(H,M))   