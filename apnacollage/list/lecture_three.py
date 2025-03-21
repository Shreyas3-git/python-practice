#list in python is collection of similar set of elements
#list uses [] braces for storing data
#list in python is mutable (we can change the values of list in python) data structure
############################
# list slicing -
# similar to string = list_name[start_index:end_index]
# when we are doing slicing with start and end index is negative
# start index will always be lesser than end index ex- start = -3,end = -1
marks = [87,64,33,95,76,"SHreys"]
print(marks)
print(marks[1:4])#here list_name[start_index:end_index] list consider starting index and end_index-1
marks = [87,64,33,95,76]
print(marks[1:]) #If end_index is missing list consider n-1 is the last index in this case
print(marks[-3:-1])

############################################
#List Methods -
list = [2,1,3]
list.append(4) # ADD ONE ELEMENT AT THE END
print(list)
list.sort() # sort in ascending order [1,2,3,4]
print(list)
list.sort(reverse=True) # sort in decending order [4,3,2,1]
print(list)
list.insert(4,10) # insert 10 at 4th index
print(list)
list.append(2)
print(list)
list.remove(2) # remove first occurence of element
print(list)
list.pop(0) # remove element based on index
print(list)
