number_1,number_2,number_3=input().split()
A=int(number_1)
B=int(number_2)
C=int(number_3)
if A>=2 and A<=10000 and B>=2 and B<=10000 and B>=2 and B<=10000:
    print((A+B)%C)
    print(((A%C)+(B%C))%C)
    print((A*B)%C)
    print((A%C)*(B%C)%C)