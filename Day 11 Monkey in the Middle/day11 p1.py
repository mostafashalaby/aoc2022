import re
troop = {}
ITEMS, MULTIPLIER, TEST, IF_TRUE, IF_FALSE, INSPECTED = 0, 1, 2, 3, 4, 5


def main():
    filename = "input.txt"
    monkeh_dnas = read(filename)
    for dna in monkeh_dnas: build_a_monkeh(dna)
    for _ in range(20): simulate()

    inspections = []
    for name in troop: inspections.append(troop[name][INSPECTED])
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n\n")
    file_handle.close()

    return lines_list


def build_a_monkeh(dna):
    surgery = dna.split("\n")
    name = re.search(r'(Monkey \d+)', surgery[0]).group(0).lower()
    items = [int(item) for item in re.findall(r'(\d+)', surgery[1])]
    multiplier = re.search(r'(?<== ).*$', surgery[2]).group(0)
    multiplier = multiplier.replace("old", "item")
    test = int(re.search(r'(\d+)', surgery[3]).group(0))
    if_true = re.search(r'(monkey \d+)', surgery[4]).group(0)
    if_false = re.search(r'(monkey \d+)', surgery[5]).group(0)
    inspected = 0

    troop[name] = [items, multiplier, test, if_true, if_false, inspected]


def simulate():
    for name, stat in troop.items():
        for item in stat[ITEMS]:
            troop[name][INSPECTED] += 1
            item = eval(stat[MULTIPLIER]) // 3 #eval takes a string and outputs python code
            throw(item, stat[IF_TRUE]) if item % stat[TEST] == 0 else throw(item, stat[IF_FALSE])
        troop[name][ITEMS] = []


def throw(item, receiver):
    troop[receiver][ITEMS].append(item)


if __name__ == "__main__":
    main()
