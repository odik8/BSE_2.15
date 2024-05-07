# open the file2.txt in append mode.
# Create a new file if no such file exists.
with open("file.txt", "w") as fileptr:
    fileptr.write(
        "Python is the modern day language. It makes things so simple."
        "It is the fastest-growing programing language"
    )
