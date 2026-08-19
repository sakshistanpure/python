#creating a list
list=[2, 'sakhi', 2.5, 5]
print(list)

#accessing elements in list
print(list[1])

#updating elements in list
list[3]=5
print(list)

#adding element to list
list.append(116)
print(list)

#insert method
list.insert(1,3)
print(list)

#extend
list.extend([1,5.5,"tanpure"])
print(list)

#removing
list.remove(116)
print(list)

#pop method
list.pop(1)
print(list)

#del keyword
del list[2]
print(list)

#length of list
print(len(list))

#in keyword
if 7 in list:
    print("Element is present")
else:
    print("Element is absent")
    
#list traversal
for i in list:
    print(i)
    
#count list
print(list.count(2))

#index method
print(list.index(5.5))

list2=[2,6,4,8,5]

#reverse method
list.reverse()
print(list)

#sort list(assending)
print(list2.sort())
print(list2)

#desending order
print(list2.sort(reverse=True))
print(list2)

#copy method
new=list.copy()
print(new)

#clear method
list.clear()
print(list)