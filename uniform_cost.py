from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.cost = {}

    def addEdgeWithCost(self, u, v, c):
        self.graph[u].append(v)
        self.cost[(u, v)] = c

    def uniform_cost_search(self, goal, start):
        answer = []
        paths = []  # Track paths to goals

        queue = []

        for i in range(len(goal)):
            answer.append(10 ** 8)
            paths.append([])  # Initialize empty paths

        queue.append([0, start, [start]])  # Include path in the queue

        visited = {}

        count = 0

        while len(queue) > 0:

            queue = sorted(queue)
            p = queue[-1]

            del queue[-1]

            p[0] *= -1

            if p[1] in goal:

                index = goal.index(p[1])

                if answer[index] == 10 ** 8:
                    count += 1

                if answer[index] > p[0]:
                    answer[index] = p[0]
                    paths[index] = p[2]  # Update path

                del queue[-1]

                queue = sorted(queue)
                if count == len(goal):
                    return answer, paths  # Return both costs and paths

            if p[1] not in visited:
                for i in range(len(self.graph[p[1]])):
                    new_path = p[2] + [self.graph[p[1]][i]]  # Extend path
                    queue.append([(p[0] + self.cost[(p[1], self.graph[p[1]][i])]) * -1, self.graph[p[1]][i], new_path])

            visited[p[1]] = 1

        return answer, paths


if __name__ == '__main__':
    g = Graph()
    goal_list = list()
    V = int(input("Enter the number of vertices: "))
    for i in range(V):
        print("Enter u v c: ")
        ip = input().split()
        g.addEdgeWithCost(int(ip[0]), int(ip[1]), int(ip[2]))
    n = int(input("Enter the number of goal nodes: "))
    for i in range(n):
        goal_list.append(int(input(f"Enter the goal node {i + 1}: ")))
    start_node = int(input("Enter start node: "))
    # g.addEdgeWithCost(0, 1, 2)
    # g.addEdgeWithCost(0, 3, 5)
    # g.addEdgeWithCost(1, 6, 1)
    # g.addEdgeWithCost(3, 1, 5)
    # g.addEdgeWithCost(3, 6, 6)
    # g.addEdgeWithCost(3, 4, 2)
    # g.addEdgeWithCost(2, 1, 4)
    # g.addEdgeWithCost(4, 2, 4)
    # g.addEdgeWithCost(4, 5, 3)
    # g.addEdgeWithCost(5, 2, 6)
    # g.addEdgeWithCost(5, 6, 3)
    # g.addEdgeWithCost(6, 4, 7)
    # goal_list.append(6)
    # start_node=0
    min_cost, paths = g.uniform_cost_search(goal_list, start_node)
    j=0
    for i, goal_node in enumerate(goal_list):
        print(f"Shortest path to goal node {goal_node} with cost {min_cost[j]} \n {paths[i]}")
        j+=1
