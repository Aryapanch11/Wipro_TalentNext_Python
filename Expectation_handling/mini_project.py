# You had saved the items and their price details in a text file, which you
# purchased yesterday from a nearby super market.
# You need to know:
# 1. How many items did you purchase?
# 2. How many items are free?
# 3. What is the total amount you had to pay?
# 4. What is the discount amount?
# 5. What is the final amount did you pay after the discount?
# Help yourself by writing a python code to do this. Include necessary code to
# handle the possible exceptions.
# Note:
# . Data is stored in a text file Purchase-1.txt.
# . Each line contains one item's details.
# . Item name and price is separated by a space.
# . You have to enter the file name during run time.

# Sample input 1:
# Purchase-1.txt
# Chocolate 50
# Biscuit 35
# Icecream 30
# (blank line)
# Discount 5

# Sample output 1:
# Enter the file name: Purchase-1
# No of items purchased: 3
# No of free items: 0
# Amount to pay: 135
# Discount given: 5
# # Final amount paid: 130

def main():
    try:
        filename = input("Enter the file name: ") + ".txt"
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_amount = 0
        discount = 0
        item_count = 0
        free_item_count = 0

        for line in lines:
            line = line.strip()
            if not line:  
                continue

            parts = line.split()
            if len(parts) == 2:
                item, value = parts[0], parts[1]
                try:
                    value = int(value)
                    if item.lower() == "discount":
                        discount = value
                    elif value == 0:
                        free_item_count += 1
                        item_count += 1
                    else:
                        total_amount += value
                        item_count += 1
                except ValueError:
                    print(f"Invalid price '{value}' for item '{item}'. Skipping.")
            else:
                print(f"Invalid line format: {line}. Skipping.")

        final_amount = total_amount - discount

        print(f"No of items purchased: {item_count}")
        print(f"No of free items: {free_item_count}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()
