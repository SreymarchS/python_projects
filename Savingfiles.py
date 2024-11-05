#Writing into a file

#Function to save a list of strings into file
def save_strings_files(strings,filename):
    with open(filename, "w")as file:
        for string in strings:
            file.write(string + "\n")

#The sample of the input strings
strings = ["Hello", "Python", "Programming", "Writing"]

#Saving the strings into output file
save_strings_files(strings, "output.txt")
