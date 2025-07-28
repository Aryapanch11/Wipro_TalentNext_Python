#  1. Create a list of 5 integers and access individual elements by index
my_list = [10, 20, 30, 40, 50]
print("Complete list:", my_list)
print("First element:", my_list[0])
print("Third element:", my_list[2])

#  2. Append a new item to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print("Updated list:", my_list)


#  3. Reverse the order of the items in the list
my_list = [10, 20, 30, 40]
my_list.reverse()
print("Reversed list:", my_list)


# 4. Print number of occurrences of a specified element in a list
my_list = [1, 2, 3, 2, 4, 2, 5]
print("Count of 2:", my_list.count(2))

#  5. Append the items of list1 to list2 in the front
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("Updated list2:", list2)

#  6. Insert a new item before the second element
my_list = [10, 30, 40]
my_list.insert(1, 20)
print("After inserting 20 at index 1:", my_list)

#  7. Remove the item from a specified index
my_list = [5, 10, 15, 20]
del my_list[2]
print("List after removing index 2:", my_list)


#  8. Remove the first occurrence of a specified element
my_list = [1, 2, 3, 2, 4]

my_list.remove(2)

print("After removing first 2:", my_list)
