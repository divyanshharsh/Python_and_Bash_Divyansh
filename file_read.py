# Read Content from a File

file_name = "output/student_data.txt"

with open(file_name, "r") as file:
    content = file.read()

print("File Content:")
print("-------------------------")
print(content)
print("-------------------------")