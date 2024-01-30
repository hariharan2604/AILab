from collections import deque


class State:
    def __init__(self, left_m, left_c, right_m, right_c, boat):
        self.left_m = left_m
        self.left_c = left_c
        self.right_m = right_m
        self.right_c = right_c
        self.boat = boat

    def is_valid(self):
        if self.left_m < 0 or self.left_c < 0 or self.right_m < 0 or self.right_c < 0:
            return False
        if (self.left_c > self.left_m > 0) or (self.right_c > self.right_m > 0):
            return False
        return True

    def is_goal(self):
        return self.left_m == 0 and self.left_c == 0

    def successors(self):
        moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
        next_states = []
        for move in moves:
            if self.boat == 'left':
                new_state = State(self.left_m - move[0], self.left_c - move[1],
                                  self.right_m + move[0], self.right_c + move[1], 'right')
            else:
                new_state = State(self.left_m + move[0], self.left_c + move[1],
                                  self.right_m - move[0], self.right_c - move[1], 'left')
            if new_state.is_valid():
                next_states.append(new_state)
        return next_states


def print_board(left_m, left_c, right_m, right_c):
    for i in range(0, left_m):
        print("M ", end="")
    for i in range(0, left_c):
        print("C ", end="")
    print("| --- | ", end="")
    for i in range(0, right_m):
        print("M ", end="")
    for i in range(0, right_c):
        print("C ", end="")
    print("\n")


def bfs(initial_state):
    visited = set()
    queue = deque([[initial_state]])
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state.is_goal():
            return path
        for succ in state.successors():
            if tuple([succ.left_m, succ.left_c, succ.right_m, succ.right_c, succ.boat]) not in visited:
                visited.add(tuple([succ.left_m, succ.left_c, succ.right_m, succ.right_c, succ.boat]))
                new_path = list(path)
                new_path.append(succ)
                queue.append(new_path)
    return None


def print_path(path):
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print_board(state.left_m, state.left_c, state.right_m, state.right_c)


def main():
    initial_state = State(3, 3, 0, 0, 'left')
    path = bfs(initial_state)
    if path:
        print("The Steps...\n")
        print_path(path)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
