#creating a program to read from a file


#Reading data from a file
with open("data.txt", "r") as file:
    content = file.read()

#Printing my data file
print("Printing the contents of Data.txt")
print(content)