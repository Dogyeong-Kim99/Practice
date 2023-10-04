N,M=map(int,input().split())
A=list(map(int,range(1,N+1)))
for _ in range(M):
    i,j=map(int,input().split())
    k=(j-i)//2+1
    for x in range(k):
        A[i-1+x],A[j-1-x]=A[j-1-x],A[i-1+x]   
print(*A)
