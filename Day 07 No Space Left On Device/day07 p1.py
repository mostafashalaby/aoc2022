def main():
    filename = "input.txt"
    lines = read(filename)
    dir_size = populate(lines)

    sum_100k = 0
    for directory, size in dir_size.items():
        if size <= 100000:
            sum_100k += size
    print(sum_100k)

    exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def populate(lines):
    dir_size = {}
    cur_dir = []
    for line in lines:
        if line[0] == '$':
            line = line[2:]

        if line == "ls":
            continue
        else:
            command, arg = line.split()

        if command == "cd":
            if arg != "..":
                cur_dir.append(arg)
            else:
                cur_dir.pop()
        else:
            if command.isdigit():
                for i in range(len(cur_dir)):
                    directory = "/".join(cur_dir[:i+1])
                    if directory not in dir_size:
                        dir_size[directory] = 0
                    dir_size[directory] += int(command)

    return dir_size


if __name__ == "__main__":
    main()
