while True:   #EOF하는 법
    try:
        A,B=input().split()
        a=int(A)
        b=int(B)
        print(a+b)
    
    except EOFError:
        break