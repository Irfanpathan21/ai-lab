# =====================================================================
# PRACTICAL 3: WATER JUG PROBLEM (Using BFS)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: State Space Search via Queue (BFS)
# CORE CONCEPT:
#   State = (x, y) where x = water in Jug 1, y = water in Jug 2.
#   Maintain queue of (current_state, path_so_far).
#   Apply 6 valid actions (Fill, Empty, Pour) to find the shortest path.
#
# EXAM ADAPTATION GUIDE:
#   - Capacities / Goal: Modify CAP_X, CAP_Y, and GOAL values.
#   - Any State Space Problem (Missionaries & Cannibals, 8-Puzzle):
#     Replace state tuple and 'rules' with valid transitions!
# =====================================================================

# 1. Capacities and Target Goal
CAP_X = 4   # Jug 1 Capacity (4 Litres)
CAP_Y = 3   # Jug 2 Capacity (3 Litres)
GOAL  = 2   # Target: Measure 2 Litres in either jug

# 2. Universal State-Space BFS Function
def water_jug(start_x=0, start_y=0):
    start = (start_x, start_y)
    queue = [(start, [start])]
    visited = {start}

    while queue:
        (x, y), path = queue.pop(0)

        # Goal Check: Does any jug have the target amount?
        if x == GOAL or y == GOAL:
            print(f"\nGoal {GOAL}L Reached! Shortest Path ({len(path)-1} steps):")
            for step in path:
                print(f"  Jug1: {step[0]}L | Jug2: {step[1]}L")
            return

        # 6 Production Rules (Fill, Empty, Pour)
        rules = [
            (CAP_X, y),                       # 1. Fill Jug 1
            (x, CAP_Y),                       # 2. Fill Jug 2
            (0, y),                           # 3. Empty Jug 1
            (x, 0),                           # 4. Empty Jug 2
            (x - min(x, CAP_Y - y), y + min(x, CAP_Y - y)),  # 5. Pour Jug 1 -> Jug 2
            (x + min(y, CAP_X - x), y - min(y, CAP_X - x))   # 6. Pour Jug 2 -> Jug 1
        ]

        for next_state in rules:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("Goal state is unreachable!")

# 3. Driver Code with User Input (default 0)
if __name__ == '__main__':
    print("Water Jug Problem (4L & 3L -> 2L Goal):")
    sx = int(input("Enter initial water in 4L jug (default 0): ").strip() or 0)
    sy = int(input("Enter initial water in 3L jug (default 0): ").strip() or 0)
    water_jug(sx, sy)
