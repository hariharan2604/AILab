from sys import maxsize
from itertools import permutations


def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    V = len(graph)
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)

    return min_path


if __name__ == "__main__":
    graph = list()
    while True:
        print("\n1. Add Cost matrix.")
        print("2. Print TSP.")
        print("3. Exit")
        flag = int(input("Enter Your Choice:"))
        if flag == 1:
            row = list(map(int, input().split()))
            graph.append(row)
        elif flag == 2:
            s = int(input("Enter the starting node: "))
            print(f"Following is the TSP distance: ")
            print(travellingSalesmanProblem(graph, s))
        elif flag == 3:
            break
        else:
            print("Invalid")
