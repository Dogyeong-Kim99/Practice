N=int(input())
A=[[]]*N
B=[""]*N
for i in range(N):
    A[i]=input()
for i in range(N):
    B[i]=A[i][0]+A[i][len(A[i])-1]
    print(B[i])
"""
문자열은 문자열로 만들어서 넣어주어야 한다
오히려 list보다 쉽게 +로 넣어주면된다.
"""