A=[False]*30
for i in range(28):
    n=int(input())
    A[n-1]=True
for i in range(30):
    if A[i]==False:
        print(i+1)
        
"""
x=list(map(int,range(1,31)))
for i in range(28):
    x.remove(int(input()))
for j in x:
    print(j)
    
remove 함수를 쓰면 편하다
"""