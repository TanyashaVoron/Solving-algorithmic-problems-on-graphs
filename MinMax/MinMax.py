import heapq
import os


def write(path, weight, output_file_name):
    with open(os.path.join(output_file_name), "w") as f:
        if not path:
            f.write("N\n")
        else:
            f.write("Y\n")
            f.write(" ".join(str(x + 1) for x in path) + "\n")
            f.write(str(weight))


def read(start_finish, input_file_name):
    with open(os.path.join(input_file_name), "r") as f:
        n = int(f.readline().strip())
        adjacency_list = [[] for _ in range(n)]
        for i in range(n):
            line = list(map(int, f.readline().strip().split()))
            while line[-1] != 0:
                line.extend(list(map(int, f.readline().strip().split())))
            for j in range(0, len(line) - 1, 2):
                adjacency_list[i].append((line[j] - 1, line[j + 1]))
        start_finish[0], start_finish[1] = int(f.readline()), int(f.readline())
    return adjacency_list


class Algorithm:
    def __init__(self, numNodes):
        self.dist = [float("inf")] * numNodes
        self.prev = [-1] * numNodes
        self.visited = [False] * numNodes
        self.graph = [[] for _ in range(numNodes)]

    def addEdge(self, frm, to, weight):
        self.graph[frm].append((to, weight))

    def findShortestPath(self, start, end):
        pq = [(0, start)]
        self.dist[start] = 0
        while pq:
            currDist, currNode = heapq.heappop(pq)
            if self.visited[currNode]:
                continue
            self.visited[currNode] = True
            for nextNode, weight in self.graph[currNode]:
                if not self.visited[nextNode] and self.dist[currNode] + weight < self.dist[nextNode]:
                    self.dist[nextNode] = self.dist[currNode] + weight
                    self.prev[nextNode] = currNode
                    heapq.heappush(pq, (self.dist[nextNode], nextNode))
        if self.dist[end] == float("inf"):
            return [], float("inf")
        else:
            max = -1
            currNode = end
            path = []
            while currNode != -1:
                path.append(currNode)
                currNode = self.prev[currNode]

                for nextNode, weight in self.graph[currNode]:
                    if nextNode == path[-1] and weight > max:
                        max = weight

            path.reverse()
            return path, max


def main():
    for i in range(4):
        input_file_name = 'In' + str(i + 1) + '.txt'
        output_file_name = 'Output' + str(i + 1) + '.txt'

        start_finish = [0, 0]
        adjacencyList = read(start_finish, input_file_name)
        dijkstra = Algorithm(len(adjacencyList))

        for k in range(len(adjacencyList)):
            for j in range(len(adjacencyList[k])):
                dijkstra.addEdge(k, adjacencyList[k][j][0], adjacencyList[k][j][1])

        path, weight = dijkstra.findShortestPath(start_finish[0] - 1, start_finish[1] - 1)
        write(path, weight, output_file_name)


if __name__ == '__main__':
    main()
