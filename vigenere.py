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
# Create a list where you'll put the character
# Gather the equivalent number of the letter based on dictionary for key and message
# add the number gathered from message and key
# Convert the gathered numbers into string and insert it in list
# Let user input it the data(uppercase, no space)
# Let the user continue the process or stop