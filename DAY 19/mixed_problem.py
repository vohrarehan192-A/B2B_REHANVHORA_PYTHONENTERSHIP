# Step 1: Write numbers to file
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

# Step 2: Read from file and print evens
print("Even numbers found in the file:")
with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip()) # Convert the text line into an integer
        if num % 2 == 0:
            print(num)
