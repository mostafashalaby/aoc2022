def main():
    filename = "input.txt"
    list_calories = read(filename)
    #print(list_calories)
    list_sum_calories = []

    max_calorie = 0
    for calorie_str in list_calories:
        int_calorie = sum_calories(calorie_str)
        if (int_calorie > max_calorie):
            max_calorie = int_calorie
        list_sum_calories.append(sum_calories(calorie_str))
    #print(list_sum_calories)
    print(max_calorie)
    return max_calorie


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n\n")
    file_handle.close()

    return lines_list

def sum_calories(calorie_str):
    sum = 0
    for calorie in calorie_str.split('\n'):
        int_calorie = int(calorie)
        sum += int_calorie

    return sum




if __name__ == "__main__":
    main()