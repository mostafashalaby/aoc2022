lines = open('input.txt', 'r').readlines()

total = 0
for line in lines:
    line = line.strip()
    s1, s2 = line.split(",")
    s1l, s1u = s1.split("-")
    s2l, s2u = s2.split("-")

    s1l, s1u = int(s1l), int(s1u)
    s2l, s2u = int(s2l), int(s2u)

    if s1l <= s2l and s2u <= s1u or s2l <= s1l and s1u <= s2u:
        total += 1

print(total)