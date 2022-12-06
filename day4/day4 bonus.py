def main():
    filename = "input.txt"
    list_pairs = read(filename)

    contained = 0
    for pair in list_pairs:
        pair = pair.strip()
        contained += check_full_containment(pair)


    print(contained)
    return exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def check_full_containment(pair):
    contained = 0
    first, second = pair.split(",")
    contained += overlap(first, second)

    return contained


def overlap(first, second):
    first_left, first_right = first.split("-")
    second_left, second_right = second.split("-")

    first_left, first_right = int(first_left), int(first_right)
    second_left, second_right = int(second_left), int(second_right)

    if second_left > first_right or first_left > second_right:
        return 0
    return 1


if __name__ == "__main__":
    main()