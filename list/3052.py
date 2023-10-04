A=[False]*42
for i in range(10):
    N=int(input())
    A[N%42]=True
count=0
for i in range(42):
    if A[i]==True:
        count=count+1
print(count)

"""
a = []
for _ in range(10):
    a.append(int(input()) % 42)
print(len(set(a)))

set을 쓰면 얼마 있는지 쉽게 파악이 가능하다
"""