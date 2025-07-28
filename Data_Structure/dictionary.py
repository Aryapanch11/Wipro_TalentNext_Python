# 1. Add a key and value to a dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)

# ✅ 2. Concatenate dictionaries to create a new one
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
merged_dict = {}
for d in (dict1, dict2, dict3):
    merged_dict.update(d)

print(merged_dict)


# 3. Check if a given key exists in a dictionary
sample_dict = {1: 10, 2: 20, 3: 30}
key_to_check = 2

if key_to_check in sample_dict:
    print("Key exists!")
else:
    print("Key does not exist.")
    
# 4. Iterate using for loop and print keys, values, and key-value pairs
sample_dict = {1: 'a', 2: 'b', 3: 'c'}
print("Keys:")
for key in sample_dict:
    print(key)
print("Values:")
for value in sample_dict.values():
    print(value)
print("Key-Value Pairs:")
for key, value in sample_dict.items():
    print(key, ":", value)
    
    
#  5. Prepare a dictionary with keys 1 to 15 and values = square of keys
squares_dict = {}
for i in range(1, 16):
    squares_dict[i] = i ** 2
print(squares_dict)


#  6. Sum all the values in a dictionary (int values only)
sample_dict = {'a': 100, 'b': 200, 'c': 300}
total = sum(sample_dict.values())
print("Sum of values:", total)
