#  Write a program to read the entire content from a txt file and display it to the user.

def read_entire_file(filename="sample.txt"):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"--- Content of {filename} ---")
            print(content)
            print(f"--- End of {filename} ---")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_entire_file()
  
#  Write a program to read first n lines from a txt file. Get n as user input. 
  
def read_first_n_lines(filename="sample.txt"):
    try:
        n_str = input("Enter the number of lines to read: ")
        n = int(n_str)
        if n < 0:
            print("Please enter a non-negative number of lines.")
            return

        with open(filename, 'r') as file:
            print(f"\n--- First {n} lines of {filename} ---")
            for i, line in enumerate(file):
                if i < n:
                    print(line.strip()) 
            print(f"--- End of first {n} lines ---")

    except ValueError:
        print("Invalid input. Please enter an integer.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_first_n_lines()
    
    
    
# Write a program to accept input from user and append it to a txt file.
    
def append_user_input_to_file(filename="output.txt"):
    user_input = input("Enter content to append to the file: ")

    try:
        with open(filename, 'a') as file:
            file.write(user_input + '\n') 
        print(f"Successfully appended to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    append_user_input_to_file()


# Write a program to read contents from a txt file line by line and store each line into a list.

def read_lines_to_list(filename="sample.txt"):
    lines_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines_list.append(line.strip()) 
        print(f"--- Lines from {filename} stored in a list ---")
        for i, line in enumerate(lines_list):
            print(f"Line {i+1}: {line}")
        print(f"\nFull list: {lines_list}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines_list

if __name__ == "__main__":
    my_lines = read_lines_to_list()
   
    
    
# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.   
import re

def find_longest_word(filename="sample.txt"):
    longest_word = ""
    max_length = 0

    try:
        with open(filename, 'r') as file:
            content = file.read()
        
            words = re.findall(r'\b\w+\b', content.lower()) 

            if not words:
                print(f"No words found in '{filename}'.")
                return None

            for word in words:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_word = word
            
            print(f"The longest word in '{filename}' is: '{longest_word}' (length: {max_length})")
            return longest_word

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

if __name__ == "__main__":
    find_longest_word()
    
#   Write a program to count the frequency of a user entered word in a txt file.   
    
import re 

def count_word_frequency(filename="sample.txt"):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower() 
           
            words = re.findall(r'\b\w+\b', content)

            if not words:
                print(f"No words found in '{filename}'.")
                return

            target_word = input("Enter the word to count: ").lower() 

            count = words.count(target_word)

            print(f"The word '{target_word}' appears {count} time(s) in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    count_word_frequency()