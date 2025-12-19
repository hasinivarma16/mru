#1st way
file_obj = open("content.txt", "r")
file_data=file_obj.read(20)
print(file_data)
file_obj.close()

#2nd way using with statement
with open("content.txt", "r") as file_obj:
    file_data=file_obj.readline()#read single line
    file_data=file_obj.readlines()#read all lines as list
    file_data=file_obj.read()#read full file
    print(file_data)

with open("content.txt", "w") as file_obj:
    file_data=file_obj.write("This is new content added to file.\n")

l=["python","java","c++"]
with open("content.txt", "w") as file_obj:
    file_obj.writelines(l)

#append mode
with open("content.txt", "a") as file_obj:
    file_obj.write("\nThis line is appended.")