#  1. Count number of uppercase and lowercase letters in a string
s = "WiproTech"
upper = 0
lower = 0
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#  2. Check whether a given string is Palindrome or not
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
#  3. Repeat first 2 chars of string n times (n = length of string)
s = "Wipro"
n = len(s)
first_two = s[:2]
result = first_two * n
print(result)


# 4. If first or last char is 'x', remove them
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

#  5. Repeat last n characters of string, n times
s = "wipro"
n = 3
last_part = s[-n:]
result = last_part * n
print(result)