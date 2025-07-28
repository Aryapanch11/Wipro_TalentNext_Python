#  1. Return the sum of all numbers in a list
def sum_of_list(numbers):
    return sum(numbers)
print(sum_of_list([8, 2, 3, 0, 7])) 

#  2. Return the reverse of a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("1234abcd"))  


# 3. Calculate and return the factorial of a number

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5)) 

#  4. Print number of uppercase and lowercase letters in a string

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
count_case("HelloWORld")  

#  5. Print even numbers from a list
def print_even_numbers(lst):
    evens = [num for num in lst if num % 2 == 0]
    print(evens)
print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) 


#  6. Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  
print(is_prime(10)) 