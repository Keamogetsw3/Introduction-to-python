# Read the contents of input.txt
with open('input.txt', 'r') as infile:
    contents = infile.read()

# Count the number of words
word_count = len(contents.split())

# Convert all text to uppercase
uppercase_text = contents.upper()

# Write the processed text and word count to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write("Processed Text:\n")
    outfile.write(uppercase_text + "\n")
    outfile.write(f"\nWord Count: {word_count}\n")

print("Success! 'output.txt' has been created with the processed text and word count.")
