# =====================================================================
# PRACTICAL 3: WATER JUG PROBLEM (Using BFS)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Problem: 4L aur 3L ke jug se 2L paani measure karna hai.
# =====================================================================

# Jug ki maximum capacities
CAP_X = 4  # Jug 1 capacity = 4 Litre
CAP_Y = 3  # Jug 2 capacity = 3 Litre
GOAL = 2   # Hume kisi bhi jug me 2 Litre chahiye

def water_jug_bfs(start_x, start_y):
    # Q1. STATE: State kaisa dikhega?
    # Answer: Ek tuple (x, y) jahan x = Jug 1 me paani, y = Jug 2 me paani.
    start_state = (start_x, start_y)

    # Q2. MEMORY: Repeated states se kaise bachein?
    # Answer:
    # 1. 'visited': Jo (x, y) combinations pehle dekh chuke hain unhe yaad rakhna.
    # 2. 'queue': BFS ke liye queue, jisme state aur path save karenge: [state, [path]]
    visited = set()
    queue = []

    # Initial state ko queue aur visited me daalo
    queue.append((start_state, [start_state]))
    visited.add(start_state)

    while queue:
        # Queue se pehla state bahar nikalo (FIFO)
        (x, y), path = queue.pop(0)

        # Q3. GOAL CHECK: Kab rukna hai?
        # Agar Jug 1 ya Jug 2 kisi me bhi 2L paani aa jaye -> Goal achieved!
        if x == GOAL or y == GOAL:
            print("\nGoal State Mil Gaya!")
            print("Pura Path (Step-by-Step):")
            for step in path:
                print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
            return

        # Q4. EXPLORATION / NEXT STEPS: Is state (x, y) se hum kya kya kar sakte hain?
        # Sirf 6 possible rules hote hain:
        rules = [
            (CAP_X, y),                       # Rule 1: Jug 1 ko poora bhar do
            (x, CAP_Y),                       # Rule 2: Jug 2 ko poora bhar do
            (0, y),                           # Rule 3: Jug 1 ko khali kar do
            (x, 0),                           # Rule 4: Jug 2 ko khali kar do
            # Rule 5: Jug 1 se Jug 2 me daalo (jitni jagah bachi hai)
            (x - min(x, CAP_Y - y), y + min(x, CAP_Y - y)),
            # Rule 6: Jug 2 se Jug 1 me daalo (jitni jagah bachi hai)
            (x + min(y, CAP_X - x), y - min(y, CAP_X - x))
        ]

        # In sabhi rules se banne wale naye states ko check karo
        for next_state in rules:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("Goal state tak nahi pahunch sake!")

# Driver Code
if __name__ == '__main__':
    print("Water Jug Problem using BFS (4L and 3L Jugs -> 2L Goal):")
    x_in = input("Enter initial water in 4L jug (default 0): ").strip()
    y_in = input("Enter initial water in 3L jug (default 0): ").strip()
    x_initial = int(x_in) if x_in else 0
    y_initial = int(y_in) if y_in else 0

    water_jug_bfs(x_initial, y_initial)
