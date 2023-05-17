def input(name_file_input):
    with open(name_file_input, 'r') as f:
        return f.readline(), f.readline()


def convert_input(str):
    dic = {'a': 'Checking_for_bipartitioning_of_a_graph_with_a_width_search', 'b': 'the_route_riding_search_in_depth', 'c': 'MinMax', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}
    return dic[str[0]] + str[1]


def convert_output(lst):
    dic = {'Checking_for_bipartitioning_of_a_graph_with_a_width_search': 'a', 'the_route_riding_search_in_depth': 'b', 'MinMax': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h'}
    for i in range(len(lst)):
        lst[i] = dic[lst[i][0]] + lst[i][1]
    return lst


def forbidden_fields(finish):
    list_forbidden_fields = []
    x, y = int(finish[0]), int(finish[1])
    list_forbidden_fields.append(str(x - 1) + str(y - 1))
    list_forbidden_fields.append(str(x + 1) + str(y - 1))
    return list_forbidden_fields


def graf(list_forbidden_fields):
    g = {}
    for x in range(1, 9):
        for y in range(1, 9):
            lits_neighbour = []

            if x + 1 < 9 and y + 2 < 9:
                lits_neighbour.append(str(x + 1) + str(y + 2))
            if x - 1 > 0 and y + 2 < 9:
                lits_neighbour.append(str(x - 1) + str(y + 2))
            if x - 2 > 0 and y + 1 < 9:
                lits_neighbour.append(str(x - 2) + str(y + 1))
            if x - 2 > 0 and y - 1 > 0:
                lits_neighbour.append(str(x - 2) + str(y - 1))
            if x - 1 > 0 and y - 2 > 0:
                lits_neighbour.append(str(x - 1) + str(y - 2))
            if x + 1 < 9 and y - 2 > 0:
                lits_neighbour.append(str(x + 1) + str(y - 2))
            if x + 2 < 9 and y - 1 > 0:
                lits_neighbour.append(str(x + 2) + str(y - 1))
            if x + 2 < 9 and y + 1 < 9:
                lits_neighbour.append(str(x + 2) + str(y + 1))

            for i in list_forbidden_fields:
                if i in lits_neighbour:
                    lits_neighbour.remove(i)
            g[str(x) + str(y)] = lits_neighbour
    return g


def dfs(graph, start, finish, visited=None):
    if visited is None:
        visited = []

    if finish not in visited:
        visited.append(start)

    if start == finish:
        for i in graph.keys():
            graph[i] = []
        return 0

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, finish, visited)

    return visited


def test():
    with open('outputCombo.txt', 'w') as f:
        for i in 'abcdefgh':
            for j in '12345678':
                for k in 'abcdefgh':
                    for l in '12345678':
                        start = i + j
                        finish = k + l
                        f.writelines('координаты\n')
                        f.writelines(start + ' ' + finish + '\n')
                        f.writelines('путь\n')

                        if start == finish:
                            f.writelines(start + '\n')
                        else:
                            start, finish = convert_input(start), convert_input(finish)
                            path = convert_output(dfs(graf(forbidden_fields(finish)), start, finish))
                            f.writelines(' '.join(path) + '\n')
                        f.writelines('\n')


def main():
    # test()
    with open('output.txt', 'w') as f:
        start, finish = input('input2.1.txt')
        if start == finish:
            f.writelines(start + finish + '\n')
        else:
            start, finish = convert_input(start), convert_input(finish)
            path = convert_output(dfs(graf(forbidden_fields(finish)), start, finish))
            for i in path:
                f.writelines(i + '\n')


if __name__ == '__main__':
    main()
