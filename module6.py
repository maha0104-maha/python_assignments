dict={'Lahya':90,'Alice':85,'siva':66,'varsha':75,'swetha':93}
a=input("enter students's name: ").capitalize()
if (a in dict):
    print(f"{a}'s marks is {dict[a]}")
else:
    print("Student not found")


#task2

list=[1,2,3,4,5,6,7,8,9,10]
list1=list[0:5]
print(f"original list:{list}")
print(f"Extracted first five elements:{list1}")
list1.reverse()
print(f"Reversed extracted elements:{list1}")
#another method
print(f"Reversed extracted elements:{list[4::-1]}")
