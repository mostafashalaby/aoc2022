import numpy
def main():
    filename = "input.txt"
    lines = read(filename)

    width = len(lines[0])
    height = len(lines)

    tree_matrix = populate(lines, width, height)
    #print(tree_matrix)

    scenic = 0

    for i in range(1, width+1):
        for j in range(1, height+1):
            cur = tree_matrix[i][j]
            lefts = []
            for l in range(0, j):
                lefts.append(tree_matrix[i][l])
            lefts.reverse()
            #print(lefts)

            rights = []
            for r in range(j+1, height+2):
                rights.append(tree_matrix[i][r])
            #print(rights)

            downs = []
            for d in range(i+1, width+2):
                downs.append(tree_matrix[d][j])
            #print(downs)

            ups = []
            for u in range(0, i):
                ups.append(tree_matrix[u][j])
            ups.reverse()
            #print(ups)

            left_view = view(cur, lefts)
            right_view = view(cur, rights)
            down_view = view(cur, downs)
            up_view = view(cur, ups)
            score = left_view * right_view * down_view * up_view
            if score > scenic:
                scenic = score


    print(scenic)


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

def view(int, list):

    view = 0
    for i in list:
        if i == -1:
            continue
        elif int > i:
            view += 1
        else:
            view += 1
            break

    return view


if __name__ == "__main__":
    main()
