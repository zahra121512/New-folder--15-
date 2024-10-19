string = input("please enter your own word :")
char = input("please enter your own charcter : ")
i = 0
count = 0

while(i < len(string)):

    if(string[i] == char):
       count = count + 1
    i = i + 1


print("the toatal number of  times is ", char," has occured = ", count)