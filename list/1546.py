N=int(input())
A=list(map(int,input().split()))
M=max(A)
B=list(map(lambda x:x/M*100,A))
print(sum(B)/N)

"""
lambda함수에 대한 보다 명확한 이해가 필요할듯

"""