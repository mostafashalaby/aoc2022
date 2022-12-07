def main():
    filename = "input.txt"
    lines = read(filename)
    dir_size = populate(lines)

    total_disk_size = 70000000
    space_available = total_disk_size - dir_size["/"]
    space_needed = 30000000 - space_available
    print(space_available)
    print(space_needed)

    candidates_for_deletion = {}
    for directory, size in dir_size.items():
        if size >= space_needed:
            candidates_for_deletion[directory] = size

    directory_to_delete = min(candidates_for_deletion, key=candidates_for_deletion.get)
    print(candidates_for_deletion[directory_to_delete])

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