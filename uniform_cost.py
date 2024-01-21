from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.cost = {}

    def addEdgeWithCost(self, u, v, c):
        self.graph[u].append(v)
        self.cost[(u, v)] = c


def uniform_cost_search(goal, start):
    global graph, cost
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
            for i in range(len(graph[p[1]])):
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        visited[p[1]] = 1

    return answer


if __name__ == '__main__':
    g = Graph()
    goal_list = list()
    while True:
        print("1. Add Edge With Cost.")
        print("2. Print Minimum Cost.")
        print("3. Add goal.")
        print("4. Exit")
        flag = int(input("Enter Your Choice:"))
        if flag == 1:
            g.addEdgeWithCost(int(input("Enter u: ")), int(input("Enter v: ")), int(input("Enter cost:")))
        elif flag == 2:
            print(f"The minimum cost is {uniform_cost_search(goal_list, int(input("Enter start node: ")))}")
        elif flag == 3:
            goal_list.append(int(input("Enter the goal node: ")))
        elif flag == 4:
            break
        else:
            print("Invalid")
