#Creating a program with numerical pattern

rows = int(input("Please enter the number of the rows "))
num = 1

for rows in range(1, rows + 1):
    print(num)
    num = num + 2