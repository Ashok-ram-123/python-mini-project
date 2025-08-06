import os

# 1. Create and write to a file
with open("testfile.txt", "w") as file:
    file.write("Hello Ashok!\n")
    file.write("This is your first file handling practice.\n")

print("Step 1: File created and written.")

# 2. Read the file
with open("testfile.txt", "r") as file:
    content = file.read()
    print("Step 2: File content is:")
    print(content)

# 3. Append new data to the file
with open("testfile.txt", "a") as file:
    file.write("Adding a new line at the end.\n")

print("Step 3: New line appended.")

# 4. Read again to confirm append
with open("testfile.txt", "r") as file:
    content = file.read()
    print("Step 4: Updated file content:")
    print(content)

# 5. Check if file exists
if os.path.exists("testfile.txt"):
    print("Step 5: File exists.")

# 6. Delete the file (careful!)
os.remove("testfile.txt")
print("Step 6: File deleted.")