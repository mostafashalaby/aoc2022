def main():
    filename = "input.txt"
    lines = read(filename)
    left, right = partition_lines(lines)
    print(left)
    print(right)

    sum_in_order = 0
    for i in range(len(lines)):
        if compare(left[i], right[i]) > 0:
            sum_in_order += i + 1
    print(sum_in_order)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n\n")
    file_handle.close()

    return lines_list


def partition_lines(lines):
    left = []
    right = []
    for line in lines:
        l, r = line.split("\n")
        l_list, r_list = eval(l), eval(r)
        left.append(l_list)
        right.append(r_list)
    return left, right


def compare(l, r):
    l = l if isinstance(l, list) else [l]
    r = r if isinstance(r, list) else [r]
    for l2, r2 in zip(l, r):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(r) - len(l)


if __name__ == "__main__":
    main()
