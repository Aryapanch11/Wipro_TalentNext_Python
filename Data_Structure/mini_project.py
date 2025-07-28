#Create a dictionary that stores the names of people as keys and a fun fact about each person as the value.
# Initialize a dictionary with three people and their respective facts.
# Print the dictionary (each name with its fact).
# Update one of the existing facts (choose any one person).
# Add one new person along with a fact.
# Print the updated dictionary again.
# Observe whether the order of elements changes after updating (Note: In Python 3.7 and above, dictionary maintains insertion order).


# Jeff: Is afraid of Dogs.
# David: Plays the piano.
# Jason: Can fly an airplane.

# Jeff: Is afraid of heights.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jill: Can hula dance.

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}
print("Original Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

people_facts["Jeff"] = "Is afraid of heights."
people_facts["Jill"] = "Can hula dance."
print("\nUpdated Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


# Given the participant’s score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.

# Sample input: [2, 3, 6, 6, 5]
# Sample output: 5

n = int(input("Enter number of scores: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))

max_score = max(scores)
while max_score in scores:
    scores.remove(max_score)

print("Runner-up score:", max(scores))


# You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.
# Student's name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.
# Formula: (sum of marks) / (no of subjects)
# Sample
# input: { "Krishna":
# [67, 68, 69),
# "Arjun":
# [70, 98, 63),
# "Malika": [52, 56, 60]}
# Sample output:
# Enter a name: Malika
# Average percentage mark: 56

student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}
name = input("Enter a name: ")
if name in student_marks:
    marks = student_marks[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", int(average))
else:
    print("Student not found.")



# Given a string of n words, help Alex to find out how many times his name appears in the string.

# Constraint:
# 1 <= n <= 200

# Sample input:
# Hi Alex WelcomeAlex Bye Alex.

# Sample output:
# 3

# Explanation:
# Alex name appears 3 times in the string.
# Hi Alex WelcomeAlex** Bye Alex.**
def count_alex_occurrences(s):
    return s.count("Alex")
input_string = "Hi Alex WelcomeAlex Bye Alex."
print(count_alex_occurrences(input_string))  
