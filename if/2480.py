A,B,C=input().split()
num_1=int(A)
num_2=int(B)
num_3=int(C)
if A==B and B==C:
    print("%d"%(10000+num_1*1000))
elif A==B or B==C :
    print("%d"%(1000+num_2*100))
elif A==C:
    print("%d"%(1000+num_1*100))
else:
    a=[num_1,num_2,num_3]
    print("%d"%(max(a)*100))