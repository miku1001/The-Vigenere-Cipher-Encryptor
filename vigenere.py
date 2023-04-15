# Create a program that will encrypt given text through Vigenère Cipher

# Import module for loading bar
from tqdm import tqdm
import time

# Create welcome greeting
name = input("Enter your name: ")
print("\033[36mThe Vigenère Cipher\033[0m".center(59, "="))
print()

# Loading Bar
for i in tqdm(range(5), desc="Loading", leave=False):
    # Simulating some processing time
    time.sleep(1)
print(f"Good day {name}\U0001F929, encrypt your message here!\U0001F447")
print("-" * 50)

# Create character dictionary
dict_char = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
             'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
             'X': 23, 'Y': 24, 'Z': 25}

# Create a list where you'll put the character
# Gather the equivalent number of the letter based on dictionary for key and message
# add the number gathered from message and key
# Convert the gathered numbers into string and insert it in list
# Let user input it the data(uppercase, no space)
# Let the user continue the process or stop