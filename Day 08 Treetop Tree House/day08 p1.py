import numpy
def main():
    filename = "input.txt"
    lines = read(filename)

    width = len(lines[0])
    height = len(lines)

    tree_matrix = populate(lines, width, height)
    print(tree_matrix)

    visible = 0

    for i in range(1, width+1):
        for j in range(1, height+1):
            cur = tree_matrix[i][j]
            #print(cur)
            lefts = []
            for l in range(0, j):
                lefts.append(tree_matrix[i][l])

            rights = []
            for r in range(j+1, height+2):
                rights.append(tree_matrix[i][r])

            downs = []
            for d in range(i+1, width+2):
                downs.append(tree_matrix[d][j])
            #downs = tree_matrix[i+1:][j]

            ups = []
            for u in range(0, i):
                ups.append(tree_matrix[u][j])
            #ups = tree_matrix[:i][j]

            if list_less_than_int(cur, lefts) or list_less_than_int(cur, rights) or list_less_than_int(cur, downs) or list_less_than_int(cur, ups):
                #print("i:{} j:{} tree: {}".format(i, j, cur))
                visible +=1

    print(visible)


def read(filename):
    file_handle = open(filename)
    lines = file_handle.read().rstrip()
    lines_list = lines.split("\n")
    file_handle.close()

    return lines_list

def populate(lines, width, height):
    tree_matrix = [[-1 for i in range(width+2)] for j in range(height+2)]

    for i in range(1, height+1):
        temp_ints = []
        for c in lines[i-1]:
                temp_ints.append(int(c))
        temp_ints.append(-1)
        tree_matrix[i] = [-1]
        tree_matrix[i].extend(temp_ints)


    return tree_matrix

def list_less_than_int(int, list):

    #print("list:{}".format(list))
    for i in list:
        if i >= int:
            #print("list didn't pass")
            return False
    #print("list passed")
    return True


if __name__ == "__main__":
    main()
