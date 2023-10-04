S=input()
N=[-1]*26
L=len(S)
for i in range(L):
    if N[ord(S[i])-97]==-1:
        N[ord(S[i])-97]=i
print(*N)