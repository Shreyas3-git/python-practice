# Tuples in Python -
# Tuples is collection of different sets of element
# immutable sequnces of values just like strings
# tuple uses () braces for storing its data
tup = ["s",99,'A',0,"N",100]
print(type(tup)) # print type of object which is tuple
print(tup)
print(tup[1:3]) #Slicing of tuple is exactly as same as list and string
# If we have single value in tuple
tup1 = (1)
print(type(tup1)) #This tuple will consider as integer interpreter will ignore braces here,
                  # To use single value assignment as tuple we have to declare tuple like this
                  # tuple = (1,)
tupl2 = (1,)
print(type(tupl2))

######################################
#Methods of tuple
tupl3 = (2,1,3,1)
print(tupl3.index(3)) # return index of first occurence of element
print(tupl3.count(1)) # count total occurences of object in tuple