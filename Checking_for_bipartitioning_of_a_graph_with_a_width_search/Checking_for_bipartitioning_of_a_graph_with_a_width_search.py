def convert_input(name_file_input):
    with open(name_file_input, 'r') as f:
        n = int(f.readline())
        graph = []

        for i in range(n):
            graph.append([])
            s = list(map(int, f.readline().split()))

            for j in range(n):
                if s[j] == 1:
                    graph[i].append(j)
    return graph


def convert_arr_color_shares(arr_color_v):
    share_1 = []
    share_2 = []

    for n in range(len(arr_color_v)):
        if arr_color_v[n] == 1:
            share_1.append(str(n + 1))
        else:
            share_2.append(str(n + 1))

    return ' '.join(share_1) + '\n0\n' + ' '.join(share_2)


def bfs(graph):
    arr_color_v = [0] * len(graph)
    queue = []

    while 0 in arr_color_v:
        start_v = arr_color_v.index(0)
        queue.append(start_v)
        arr_color_v[start_v] = 1

        while queue:
            s = queue.pop(0)

            for neighbour in graph[s]:
                if arr_color_v[s] == arr_color_v[neighbour]:
                    return 'N'

                if arr_color_v[neighbour] == 0:
                    arr_color_v[neighbour] = -1 * arr_color_v[s]
                    queue.append(neighbour)

    return 'Y' + '\n' + convert_arr_color_shares(arr_color_v)


def main():
    with open('output1.txt', 'w') as f:
        f.write(bfs(convert_input('input1.1.txt')))

    with open('output2.txt', 'w') as f:
        f.write(bfs(convert_input('input1.2.txt')))


if __name__ == '__main__':
    main()
