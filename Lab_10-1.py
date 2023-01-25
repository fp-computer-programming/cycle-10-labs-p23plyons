# Author: PCL 1/20/23

#First user input (incase they choose to immediately input -1 and print the sum)
y = input("Please input any number you would like to add to the list or negative one to stop adding and print the sum: ")

#setting the input from a string to a intiger
y = int(y)

#creating a sum
sum = 0

#ending the code and printing the sum incase of immediate innput of -1
if (y == -1):
    print(sum)

#adding the first value to the sum
sum += y

#having the loop run 
while (y != -1):
    x = input("Please input another number you would like to add to the sum or negative one to stop adding and print the sum: ")
    x = int(x)
    if(x == -1):
        print(sum)
        break
    sum += x
    

