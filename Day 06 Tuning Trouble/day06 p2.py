def main():
    filename = "input.txt"
    line = read(filename)

    message = 14
    for i in range(0, len(line) - 13):
        list_c = []
        for x in range(i, i + 14):
            list_c.extend(line[x])
        if len(set(list_c)) == len(list_c):
            print(message)
            break
        message +=1

    exit(1)


def read(filename):
    file_handle = open(filename)
    line = file_handle.read().rstrip()
    file_handle.close()

    return line


if __name__ == "__main__":
    main()