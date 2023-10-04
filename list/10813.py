N,M=map(int,input().split())
A=[]
for i in range(N):
    A.append(i+1)
temp=0
for x in range(M):
    j,k=map(int,input().split())
    temp=A[j-1]
    A[j-1]=A[k-1]
    A[k-1]=temp
print(*A)


"""
buckets[a-1], buckets[b-1] = buckets[b-1], buckets[a-1] 
이런 식으로 간단히 표기할 수 있다
"""