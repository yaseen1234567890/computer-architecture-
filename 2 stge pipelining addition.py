a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=4
f=0
ch=int(input("1.Add, 2.Sub, 3.Mul, 4.Div : "))
if ch==1:
    res=a+b
elif ch==2:
    res=a-b
elif ch==3:
    res=a*b
elif ch==4:
    if b==0:
        print("Denominator can't be zero")
        print("Wrong input")
        f=1
    else:
        res=a/b
else:
    print("Wrong input")
    f=1
if f==0:
    print("The cycle value is",c)
    ins=int(input("Enter no of instructions:"))
    print("The Performance Measure :",ins/c)
    print("res =",res)

