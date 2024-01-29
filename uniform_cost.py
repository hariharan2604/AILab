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

        queue = []

        for i in range(len(goal)):
            answer.append(10 ** 8)

        queue.append([0, start])

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

                del queue[-1]

                queue = sorted(queue)
                if count == len(goal):
                    return answer

            if p[1] not in visited:
                for i in range(len(self.graph[p[1]])):
                    queue.append([(p[0] + self.cost[(p[1], self.graph[p[1]][i])]) * -1, self.graph[p[1]][i]])

            visited[p[1]] = 1

        return answer


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
    print(f"The minimum cost is {g.uniform_cost_search(goal_list, int(input("Enter start node: ")))[0]}")
