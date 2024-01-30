from collections import defaultdict, OrderedDict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth, path, visited):

        if src == target:
            path.append(src)
            return True

        if maxDepth <= 0:
            return False

        visited.add(src)
        for i in self.graph[src]:
            if i not in visited and self.DLS(i, target, maxDepth - 1, path, visited):
                path.append(src)
                return True
        return False

    def IDDFS(self, src, target, maxDepth):

        for depth in range(maxDepth + 1):
            visited = set()
            path = []  # Initialize path as a list
            if self.DLS(src, target, depth, path, visited):
                path.append(src)  # Add source to the path
                ordered_path = list(OrderedDict.fromkeys(path))
                ordered_path.reverse()
                # Convert path list to set
                print("Traversal Path:", " -> ".join(map(str, ordered_path)))
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
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # g.addEdge(2, 5)
    # g.addEdge(2, 6)
    # target = 6; maxDepth = 3; src = 0
    if g.IDDFS(src, target, maxDepth):
        print("Target is reachable from source " +
              "within max depth")
    else:
        print("Target is NOT reachable from source " +
              "within max depth")
