def main():
    filename = "input.txt"
    line = read(filename)

    packet = 4
    for i in range(0, len(line) - 3):
        list_c = line[i] + line[i+1] + line[i+2] + line[i+3]
        if len(set(list_c)) == len(list_c):
            print(packet)
            break
        packet +=1

    exit(1)


def read(filename):
    file_handle = open(filename)
    line = file_handle.read().rstrip()
    file_handle.close()

    return line


if __name__ == "__main__":
    main()