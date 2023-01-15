def create_file(dictionary, name):
    file = open(name, "a")
    for line in dictionary:
        print(dictionary[line])
        file.write(str(line) + ': ' + dictionary[line] + "\n")

    file.close()
    print(file.read)

dictionary = {1: "one", 2: "two"}
create_file(dictionary, "first.txt")

