from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


if __name__ == '__main__':
    g = Graph()
    goal_list = list()
    V = int(input("Enter the number of vertices: "))
    for i in range(V):
        print("Enter u v : ")
        ip = input().split()
        g.addEdge(int(ip[0]), int(ip[1]))
    print(f"Following is Depth First Traversal")
    g.DFS(int(input("Enter the start node: ")))


