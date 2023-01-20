# Author: PCL 1/20/23
y = input("Please input any number you would like to add to the list: ")

y = int(y)

sum = 0

if (y == -1):
    print(sum)

sum += y

while (y != -1):
    x = input("Please input another number you would like to add to the sum or negative one to stop adding and print the sum: ")
    x = int(x)
    if(x == -1):
        print(sum)
        break
    sum += x
    

