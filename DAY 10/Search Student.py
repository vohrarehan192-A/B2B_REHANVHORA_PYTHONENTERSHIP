students = [
    {"Name": "ayan", "Marks": 75},
    {"Name": "faiz", "Marks": 82},
    {"Name": "aban", "Marks": 88}
]

search_name = input("Enter student name to search: ")
found = False

for student in students:
    # We use .lower() to make the search case-insensitive
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break # Exit loop once found

if not found:
    print("Student Not Found")
