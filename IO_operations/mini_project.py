# Your friend has sent you a text file containing n lines. He sent a secret message
# with it, which tells you the place and time where you have to go and meet him.

# He challenges you to find it out without seeing the content of the file. He has
# given hints to find it. Let's surprise him by breaking the challenge with our

# Hints to find the secret message:
# 1. The number of lines in the file tells you the meeting time.
# Note: 1 <= number of lines <= 24
# If the number of lines is exceeding 12, you need to convert it to 12 hour
# format. For example,
# . If the number of lines is 15, then the meeting time is 3 PM.
# . If the number of lines is 10, then the meeting time is 10 AM.
# 2. The word appearing for the maximum number of times tells you the
# meeting place.
# Note: Meeting place will be a street name.
# For example,
# . If the word Oxford appears for the maximum number of times,
# then meeting place is Oxford Street.
# . If the word Park appears for the maximum number of times, then
# meeting place is Park Street.Sample input 1:
# Sample.txt
# Cricket, a bat-and-ball park game played between two teams of eleven park
# players on a field at the park center of which is a 20-metre (22-yard) pitch with
# a wicket at each end, each park comprising two bails balanced on three stumps.
# The batting park scores runs by striking the ball bowled at the park wicket with
# the park bat, while the bowling and park fielding side tries to prevent this and
# dismiss each park player (so they are "out"). Means of park include being
# bowled, when the ball hits the park and dislodges the bails, and by the fielding
# side park the ball after it is hit by the bat, but before it hits the park. When ten
# park have been dismissed, the innings ends and the teams park roles.

# Sample output 1:
# Meeting time: 9 AM
# Meeting place: Park Street
# Explanation: Number of lines is 9. The word park appears for the maximum of
# # 15 times.
import string
from collections import Counter

def decode_secret_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        if num_lines == 0:
            print("The file is empty.")
            return

        if num_lines <= 12:
            meeting_time = f"{num_lines} AM"
        else:
            meeting_time = f"{num_lines - 12} PM"

        all_words = []
        for line in lines:
            cleaned = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = cleaned.split()
            all_words.extend(words)

        if not all_words:
            print("No words found to determine meeting place.")
            return

        word_freq = Counter(all_words)
        most_common_word, freq = word_freq.most_common(1)[0]
        meeting_place = most_common_word.capitalize() + " Street"

        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = input("Enter the file name: ") 
decode_secret_message(file_name)
