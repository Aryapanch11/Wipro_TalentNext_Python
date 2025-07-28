import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <likes> <dislikes> <numbers_given>")
else:
    likes = set(sys.argv[1].split('-'))
    dislikes = set(sys.argv[2].split('-'))
    numbers = sys.argv[3].split('-')

    happiness = 0

    for num in numbers:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1

    print(happiness)