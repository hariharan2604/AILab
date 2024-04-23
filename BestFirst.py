import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def greedy_best_first_search(self, start, goal, heuristic):
        visited = set()
        pq = [(heuristic(start), start)]
        # print(pq)
        # print(self.graph)
        while pq:
            _, current_node = heapq.heappop(pq)
            print(current_node)
            if current_node == goal:
                return True  # Goal found
            visited.add(current_node)
            for neighbor, _ in self.graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic(neighbor), neighbor))

        return False  # Goal not found


# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'F', 4)


# Define a simple heuristic function (distance from node to goal)
def heuristic(node):
    distances = {'A': 8, 'B': 6, 'C': 4, 'D': 3, 'E': 2, 'F': 0}  # Example distances to the goal
    return distances.get(node, float('inf'))  # If the node is not found in distances, return infinity


start_node = 'A'
goal_node = 'F'
found = graph.greedy_best_first_search(start_node, goal_node, heuristic)

if found:
    print(f"Goal '{goal_node}' found starting from '{start_node}'.")
else:
    print(f"Goal '{goal_node}' not found starting from '{start_node}'.")
