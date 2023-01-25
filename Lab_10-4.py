# Author: PCL 1/23/23

def indexed_names (names):
    for index, vars in enumerate(names):
        #breaking each name into a list so that charcters can be added to the beginning of the strings
        namex = [*vars] 
        #recombining the lists into a string
        namex.insert(0, str(index)+": ")
        names[index] = "".join(namex)
    return (names)

#Test Case 1
print(indexed_names(["John", "Jane", "Bob"]))

#Test Case 2
print(indexed_names(["Jan", "Sean", "Collin", "Tanner", "Richie", "Joe", "Robbie", "Jack"]))