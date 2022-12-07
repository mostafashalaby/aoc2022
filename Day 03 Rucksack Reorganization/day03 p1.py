def main():
    filename = "input.txt"
    list_moves = read(filename)
    print(list_moves)

    total_priority = 0
    priority_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for compartment in list_moves:
        total_priority += give_priority(priority_list, compartment)

    print(total_priority)

    return exit(1)



def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list

def give_priority(priority_list, compartment):
    firstpart, secondpart = compartment[:len(compartment) // 2], compartment[len(compartment) // 2:]
    common = set(firstpart).intersection(set(secondpart))
    return priority_list.index(str(common)[2]) + 1


if __name__ == "__main__":
    main()