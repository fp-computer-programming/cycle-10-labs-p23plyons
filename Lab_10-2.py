# Author: PCL 1/20/23

y = input("Please input another number you would like to add to the sum: ")

y = int(y)

list = []

if (y == -1):
    print(list)
if (y%3 == 0):
    list.append(y)

while (y != -1):
    x = input("Please input another number you would like to add to the list or negative one to stop adding numbers and print all of the multiples of three from the list: ")
    x = int(x)
    if(x == -1):
        print(list)
        break
    if (x%3 == 0):
        list.append(x)