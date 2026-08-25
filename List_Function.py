Number = [7,9,5,6,3,4,5,7,4,2,8,1]
print("Print the list")
print(Number)

#Print list with new number
print("\nPrint list with some extra number")
print(Number+[11,12,13,14,15])

#Count a number
print("\nCounting the value 4")
value = Number.count(4)
print(value)

#Sort the list
Number.sort()
print("\nSorting")
print(Number)

#Finding the index of any number
ind = Number.index(8)
print("\nFinding the index of 8")
print(ind)

#Find the length of the list
length = len(Number)
print("\nLength of list")
print(length)

#Removing any number from the list
Number.remove(5)
print("\nRemoving the value 5")
print(Number)
#Reverse the list
Number.reverse()
print("\nReverse")
print(Number)

#Delete the last value from the list
Number.pop()
print("\nPop")
print(Number)

#Inserting a value to the list
Number.insert(4,100)
print("\nInserting 100")
print(Number)

#Number Add to the list
Number.append(10)
print("\nAdding 10 to the list")
print(Number)

#Clear the list
Number.clear()
print("\nClearing")
print(Number)

#Add some new number to the list
print("\nAdding some new value")
i = 1
while i<=10:
    Number.append(i)
    i = i+1
print(Number)    

#Copying the list to another list
Number2 = Number.copy()
print("\nCopying the list to the another list")
print(Number2)
