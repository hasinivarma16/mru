
with open("content.txt", "r") as file_obj:
    data = file_obj.read(20)
    print("First 20 characters:")
    print(data)

with open("content.txt", "r") as file_obj:
    data = file_obj.read()
    print("\nFull file content:")
    print(data)


with open("content.txt", "w") as file_obj:
    file_obj.write("This is new content added to file.\n")
    file_obj.write("File handling in Python.\n")


languages = ["python\n", "java\n", "c++\n"]
with open("content.txt", "w") as file_obj:
    file_obj.writelines(languages)


with open("content.txt", "a") as file_obj:
    file_obj.write("This line is appended.\n")