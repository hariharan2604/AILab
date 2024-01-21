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
    while True:
        print("1. Add Edge.")
        print("2. Print DFS.")
        print("3. Exit")
        flag = int(input("Enter Your Choice:"))
        if flag == 1:
            g.addEdge(int(input("Enter u: ")), int(input("Enter v: ")))
        elif flag == 2:
            print(f"Following is Depth First Traversal")
            g.DFS(int(input("Enter the start node: ")))
        elif flag == 3:
            break
        else:
            print("Invalid")
