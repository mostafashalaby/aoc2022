def main():
    filename = "input.txt"
    list_moves = read(filename)

    total_priority = 0
    priority_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i, compartment in enumerate(list_moves):
        if i % 3 == 0:
            total_priority += give_priority(priority_list, list_moves[i], list_moves[i+1], list_moves[i+2])
    print(total_priority)

    return exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def give_priority(priority_list, cmp1, cmp2, cmp3):
    #print(cmp1, cmp2, cmp3,)
    common = set(cmp1) & set(cmp2) & set(cmp3)
    #print(common)

    return priority_list.index(str(common)[2]) + 1


if __name__ == "__main__":
    main()