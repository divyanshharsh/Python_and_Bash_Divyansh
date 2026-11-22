# Write Content to a File

file_name = "output/student_data.txt"

content = """Python and Bash Assignment
Student: Divyansh Harsh

This file was created using Python file handling.
The program demonstrates how to open a file in write mode
and write content using the write() function.
"""

with open(file_name, "w") as file:
    file.write(content)

print(f"Content successfully written to {file_name}")