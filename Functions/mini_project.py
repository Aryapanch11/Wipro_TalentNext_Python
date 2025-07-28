# Write a Python function that accepts a hyphen-separated sequence of colors and returns them sorted alphabetically, still hyphen-separated.


def sort_colors(color_string):
    
    colors = color_string.split('-')
    colors.sort()
    return '-'.join(colors)

input1 = "green-red-yellow-black-white"
input2 = "PINK-BLUE-TAN-PURPLE"

print(sort_colors(input1))  
print(sort_colors(input2))  
