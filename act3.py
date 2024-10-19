num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
for i in range(num1, num2+1):
    for j in range(1 , 11):
        print(i, "*", j, "=", i*j)
    print()