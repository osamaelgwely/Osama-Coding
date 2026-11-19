mylist = list(("osama", "elgwely", "pilot"))
my_tuple = (10,20,200,2)
plist = [22,"OSAMA",2.19,True,[1,2,3]]
numbers = list(range(1,6))
print(mylist)
print(list(my_tuple))
print(numbers)
if "osama" in mylist:
    print("Yes, 'osama' is in the list")
else:
    print("NO")

#list[start:stop:step]
L = [0,1,2,3,4,5]
print(L[::2])
print(L[1::2])
print(L[0:4:2])
print(L[-1:0:-2])