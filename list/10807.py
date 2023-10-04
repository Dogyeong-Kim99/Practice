N=int(input())
A=input().split()
v=int(input())
check=0
for i in range(N):
    if v==int(A[i]):
        check+=1
print(check)

"""
map(int,input().split()) 이걸 쓰면 하나하나 넣기가 편하다
A = list(map(int,input().split()))
"""