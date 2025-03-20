list = []
n = input("Enter size of list")
print("Enter number")
for i in range(int(n)):
    x = (input())
    list.append(x)
list1 = list
list1.reverse()
if(list == list1):
    print("Yes")
else:
    print("No")