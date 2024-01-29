from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):

        if src == target: return True

        if maxDepth <= 0: return False

        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):

        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False


if __name__ == '__main__':
    g = Graph()
    V = int(input("Enter the number of vertices: "))
    for i in range(V):
        print("Enter u v : ")
        ip = input().split()
        g.addEdge(int(ip[0]), int(ip[1]))
    target = int(input("Enter the target: "))
    maxDepth = int(input("Enter the maximum depth: "))
    src = int(input("Enter the Start node: "))
    if g.IDDFS(src, target, maxDepth):
        print("Target is reachable from source " +
              "within max depth")
    else:
        print("Target is NOT reachable from source " +
              "within max depth")




