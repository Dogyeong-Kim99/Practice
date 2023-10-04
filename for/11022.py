import sys
T=int(sys.stdin.readline().rstrip()) #input을 할 경우 속도가 느릴 경우가 있기 때문 .rstrip()을 넣는 이유는 \n을 빼고 문자열만 넣고 싶기 때문이다.
for i in range(T):
    a,b=sys.stdin.readline().rstrip().split()
    num_1=int(a)
    num_2=int(b)
    print("Case #%d:"%(i+1),num_1,"+",num_2,"=",num_1+num_2)