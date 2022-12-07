import re

s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []

index_of_stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

def main():
    filename = "input.txt"
    list_stacks = read(filename)

    procedure = False

    for item in list_stacks:
        if item == "":
            procedure = True
            pop_stacks()
            reverse_stacks()
            continue
        if not procedure:
            item = item.ljust(36)
            populate_stacks(item)
        if procedure:
            do_algo(item)

    s = ""

    for stck in index_of_stacks:
        s += stck.pop()

    print(s)

    exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def populate_stacks(item):
    item_split = [item[i:i + 4] for i in range(0, len(item), 4)]

    for a in range(1, 10):
        if item_split[a-1] != '    ':
            index_of_stacks[a-1].append(item_split[a-1][1])


def pop_stacks():
    for a in range(1, 10):
        index_of_stacks[a-1].pop()


def reverse_stacks():
    for a in range(1, 10):
        index_of_stacks[a-1].reverse()


def do_algo(item):
    numbers = re.findall(r'\d+', item)

    move = int(numbers[0])
    frm = int(numbers[1])
    to = int(numbers[2])

    for i in range(move):
        popped = index_of_stacks[frm-1].pop()
        index_of_stacks[to-1].append(popped)


if __name__ == "__main__":
    main()