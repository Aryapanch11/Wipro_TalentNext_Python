#  1. Print 4th element from start & 4th element from end in a tuple
my_tuple = (10, 20, 30, 40, 50, 60, 70)
print("4th element from start:", my_tuple[3])
print("4th element from last:", my_tuple[-4])


#  2. Check whether an element exists in a tuple
my_tuple = (10, 20, 30, 40)
element = 20

if element in my_tuple:
    print("Element exists in tuple.")
else:
    print("Element does not exist.")
    
    
#  3. Convert a list into a tuple
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)

print("Tuple:", my_tuple)


#  4. Find the index of an item in a tuple
my_tuple = (5, 10, 15, 20, 25)
item = 20
index = my_tuple.index(item)

print(f"Index of {item} is:", index)


#  5. Replace last value of tuples in a list with 100
my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in my_list]

print(updated_list)