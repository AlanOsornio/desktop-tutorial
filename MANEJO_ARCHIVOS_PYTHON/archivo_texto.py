# Open file in write mode and write to it
with open('text_file.txt', 'w') as file:
    file.write("This is an example line.\n")

# Read the file
with open('text_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Open file in append mode and add a new line
with open('text_file.txt', 'a') as file:
    file.write("This is an additional line.\n")
