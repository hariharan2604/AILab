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
    goal_list = list()
    V = int(input("Enter the number of vertices: "))
    for i in range(V):
        print("Enter u v : ")
        ip = input().split()
        g.addEdge(int(ip[0]), int(ip[1]))
    print(f"Following is Breadth First Traversal")
    g.BFS(int(input("Enter the start node: ")))



