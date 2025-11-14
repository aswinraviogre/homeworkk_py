import os

filename = "students.txt"

count = int(input("How many student names do you want to add? "))

if os.path.exists(filename):
    print("\nExisting student names:")
    with open(filename, "r") as file:
        existing = file.read().strip()
        if existing:
            print(existing)
        else:
            print("(No names yet)")
else:
    print("\nstudents.txt does not exist. It will be created.")

new_names = []
print("\nEnter the student names:")
for _ in range(count):
    name = input()
    new_names.append(name)

with open(filename, "a") as file:
    for name in new_names:
        file.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as file:
    print(file.read())
