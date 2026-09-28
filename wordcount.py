# wordcount.py — reads a text file and prints how many words it contains

with open("sample.txt", "r") as file:   # open the file for reading
    text = file.read()                   # whole file into one string

words = text.split()                     # split on whitespace -> list of words
count = len(words)                        # how many items in the list

print(f"Word count: {count}")
