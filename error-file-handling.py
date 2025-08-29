# reading the content from a file

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Open a file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")
    file.write("Goodbye, world!\n")

with open("file.txt", "w") as file:
    file.write("if this shows then it works!!!")


# appending to a file
with open("example.txt", "a") as file:
    file.write("This line will be added at the end.\n")

# error handling

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

# Handle file not found error
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

# Handle permission errors (can't read the file)
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")

# Catch any other unexpected errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")
