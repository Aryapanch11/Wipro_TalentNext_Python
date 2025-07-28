# Write a program to accept two numbers as command line arguments and display their sum

import sys
if len(sys.argv) != 3:
    print("Usage: python script_name.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print("Sum:", total)



# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
import os 

def main():
   
    if len(sys.argv) < 2:
        print("Usage: python welcome_message.py <your_welcome_message>")
        sys.exit(1)
    script_filename = os.path.basename(sys.argv[0]) 
    welcome_message = " ".join(sys.argv[1:])

    print(f"File Name: {script_filename}")
    print(f"Welcome Message: {welcome_message}")

if __name__ == "__main__":
    main()
    
    
# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them

import sys
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    if len(sys.argv) != 11:
        print("Usage: python sum_primes.py <num1> <num2> ... <num10>")
        print("Please provide exactly 10 numbers.")
        sys.exit(1)

    numbers = []
    try:
        for i in range(1, 11):
            numbers.append(int(sys.argv[i]))
    except ValueError:
        print("Error: All arguments must be valid integers.")
        sys.exit(1)

    sum_of_primes = 0
    prime_numbers_found = []

    print("Checking numbers for primality:")
    for num in numbers:
        if is_prime(num):
            sum_of_primes += num
            prime_numbers_found.append(num)
            print(f"  {num} is prime.")
        else:
            print(f"  {num} is not prime.")

    print(f"\nNumbers provided: {numbers}")
    print(f"Prime numbers found: {prime_numbers_found}")
    print(f"Sum of prime numbers: {sum_of_primes}")

if __name__ == "__main__":
    main()