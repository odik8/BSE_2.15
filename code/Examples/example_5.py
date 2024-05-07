with open("newfile.txt", "x") as fileptr:
    print(fileptr)

    if fileptr:
        print("File created successfully")
