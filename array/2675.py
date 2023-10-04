T=int(input())
S=[""]*T
R=[""]*T
for i in range(T):
    R[i],S[i]=input().split()
for i in range(T):
    s=""
    for j in range(len(S[i])):
        s=s+S[i][j]*int(R[i])
    print(s)