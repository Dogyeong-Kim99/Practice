N=int(input())
A=list(map(int,input().split()))
B=[]
max=A[0]
min=A[0]
for i in range(N):
    if max<A[i]:
        max=A[i]
    if min>A[i]:
        min=A[i]
        
print(min,max)

#  min(A),min(B) 하면 더 편하다