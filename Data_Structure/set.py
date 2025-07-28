#  1. Write a program to remove a given item from the set.
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)

#  2. Write a program to create an intersection of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
intersection = set1 & set2  
print("Intersection of sets:", intersection)


#  3. Write a program to create a union of sets.
set1 = {10, 20, 30}
set2 = {30, 40, 50}
union_set = set1 | set2  
print("Union of sets:", union_set)


#  4. Write a program to find the maximum and minimum value in a set.
my_set = {5, 10, 25, 1, 15}
min_val = min(my_set)
max_val = max(my_set)

print("Minimum value:", min_val)