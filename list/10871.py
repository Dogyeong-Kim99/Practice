N,X=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in range(N):
    if A[i]<X:
        B.append(A[i])
print(*B) #이렇게 해야 리스트가 안 나오고 하나씩 나온다.