#  Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
def safe_division():
    try:
        num1_str = input("Enter the first number (numerator): ")
        num2_str = input("Enter the second number (denominator): ")

        num1 = float(num1_str)
        num2 = float(num2_str)

        result = num1 / num2
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        
        print(f"The result of {num1} / {num2} is: {result}")

if __name__ == "__main__":
    safe_division()
    
    
# Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
def is_prime(num):
    """Checks if a number is prime."""
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

def check_prime_with_input():
    try:
        num_str = input("Enter an integer to check if it's prime: ")
        num = int(num_str) 
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_prime_with_input()
    
# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
def read_file_in_title_case():
    filename = input("Enter the file name (e.g., sample.txt): ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            title_case_content = content.title() 
            print(f"\n--- Content of '{filename}' in Title Case ---")
            print(title_case_content)
            print(f"--- End of file content ---")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure the file exists and the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

if __name__ == "__main__":
    read_file_in_title_case()
    
#  Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
def check_list_index_value():
    my_list = [10, -5, 0, 15, -20, 30, -1, 7, 25, -100] 

    print(f"My list: {my_list}")
    print(f"Valid indices are from 0 to {len(my_list) - 1}.")

    try:
        index_str = input(f"Enter an index (0 to {len(my_list) - 1}): ")
        index = int(index_str) 
        value = my_list[index]

        if value > 0:
            print(f"The number at index {index} ({value}) is a positive number.")
        elif value < 0:
            print(f"The number at index {index} ({value}) is a negative number.")
        else: 
            print(f"The number at index {index} ({value}) is zero.")
            
    except ValueError:
        print("Error: Invalid input. Please enter an integer for the index.")
    except IndexError:
        print(f"Error: Index out of bounds. Please enter an index between 0 and {len(my_list) - 1}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_list_index_value()