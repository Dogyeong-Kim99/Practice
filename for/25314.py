N=int(input())
n=int(N/4) #python에서 나눗셈 연산은 기본적으로 실수형으로 반환 그로 인하여 정수형을 사용하려면 int()함수가 필요하다.
"""
for i in range(n):
    print("long",end=" ") #python에서 자동으로 end가 \n으로 저장되어 있다. 이걸 해결해주려면 왼쪽과 같이 end를 써서 새로 지정해주면 된다.
"""
print("long "*n+"int")#출력할때 '+' 또는 ','를 쓰면된다.