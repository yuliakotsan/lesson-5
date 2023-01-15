def dictionary_from_file(name):
    dictionary = {}
    with open(name) as file:
        for line in file:
            print(line)
            a = line.replace("\n", "").split(": ")
            if len(a) > 1:
                dictionary[int(a[0])] = a[1]

    return dictionary

print(dictionary_from_file("first.txt"))
