# Author: PCL 1/23/23

def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)

print()

#Checking for only integers
print(double_stuff([1,7,20]))

#Checking for integer and float values
print(double_stuff([2,"lizard",365]))

#Checking for integer, string, and float values
print(double_stuff(["bird",2,1.75]))