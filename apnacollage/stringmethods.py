name = "Tony Stark"
print(name.upper())
print(name.lower())
print(name.find('S'))
if (name == "Tony Stark"):
    name = name.replace("Stark","Iron Man")
else:
    name = name.replace("Stark","Ultron")
print("name:",name)

print('n' in name)