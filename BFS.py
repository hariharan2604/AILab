from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)

        queue = list()

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()
    while True:
        print("1. Add Edge.")
        print("2. Print BFS.")
        print("3. Exit")
        flag = int(input("Enter Your Choice:"))
        if flag == 1:
            g.addEdge(int(input("Enter u: ")), int(input("Enter v: ")))
        elif flag == 2:
            print(f"Following is Breadth First Traversal")
            g.BFS(int(input("Enter the start node: ")))
        elif flag == 3:
            break
        else:
            print("Invalid")
