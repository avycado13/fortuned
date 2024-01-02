import random
import sys

# Define lists of phrases that can be combined to create fortunes
subjects = ["You", "A close friend", "A stranger", "Your loved one", "Your pet"]
verbs = ["will find", "will discover", "will receive", "will enjoy", "will achieve"]
objects = ["happiness", "success", "a surprise", "good health", "a hidden talent"]
places = ["in an unexpected place", "at work", "at home", "in nature", "on a journey"]

fortunes = []

# Generate 200 unique fortunes
for i in range(400):
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    fobject = random.choice(objects)
    place = random.choice(places)
    
    fortune = f"{subject} {verb} {fobject} {place}."
    fortunes.append(fortune)

# Read the existing fortunes from the file
with open('fortunes.txt', 'r') as f:
    existing_fortunes = f.read().splitlines()

# Open the file in append mode ('a')
with open('fortunes.txt', 'a') as f:
    for item in fortunes:
        # Check if the item is not already in the file
        if item not in existing_fortunes:
            # Write each item on a new line
            f.write("%s\n" % item)
