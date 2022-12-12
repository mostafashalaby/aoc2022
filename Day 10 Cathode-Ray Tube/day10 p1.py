signal_strength_list = []
LIMIT = 220

def main():
    filename = "input.txt"
    lines = read(filename)

    cycle = 0
    x = 1
    for line in lines:
        if line == "noop":
            cycle += 1
            check_signal_strength(cycle, x, LIMIT)
        else:
            addx, v = line.split(" ")
            cycle += 1
            check_signal_strength(cycle, x, LIMIT)
            cycle += 1
            check_signal_strength(cycle, x, LIMIT)
            x += int(v)

    print(sum(signal_strength_list))
    exit(1)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list


def check_signal_strength(cycle, x, limit):
    if cycle <= limit and cycle % 40 == 20:
        signal_strength = cycle * x
        signal_strength_list.append(signal_strength)


if __name__ == "__main__":
    main()
