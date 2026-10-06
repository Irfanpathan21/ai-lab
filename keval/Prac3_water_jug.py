#Water_Jug(BFS)
def transferXY(x, y):
    # Transfer water from X (4L) to Y (3L)
    if x + y > 3:
        x = x - (3 - y)
        y = 3
    else:
        y = x + y
        x = 0
    return x, y


def transferYX(x, y):
    # Transfer water from Y (3L) to X (4L)
    if x + y > 4:
        y = y - (4 - x)
        x = 4
    else:
        x = x + y
        y = 0
    return x, y


def waterJug(x, y):
    st.append((x, y))

    while st:
        x1, y1 = st.pop()

        if (x1, y1) in visited:
            continue

        print("Node :", (x1, y1))
        visited.append((x1, y1))

        # Goal State
        if x1 == 2 or y1 == 2:
            print("\nGoal State Reached!")
            return

        # Fill 4L Jug
        if x1 < 4:
            st.append((4, y1))

        # Fill 3L Jug
        if y1 < 3:
            st.append((x1, 3))

        # Empty 4L Jug
        if x1 > 0:
            st.append((0, y1))

        # Empty 3L Jug
        if y1 > 0:
            st.append((x1, 0))

        # Transfer X -> Y
        if x1 > 0 and y1 < 3:
            st.append(transferXY(x1, y1))

        # Transfer Y -> X
        if y1 > 0 and x1 < 4:
            st.append(transferYX(x1, y1))

        print("Stack :", st)


# ---------------- Main ----------------

x = int(input("Enter Initial State of 4 litre Jug : "))
y = int(input("Enter Initial State of 3 litre Jug : "))

visited = []
st = []

if x == 2 or y == 2:
    print("Initial state is the Goal State")
else:
    waterJug(x, y)

print("\nVisited States:")
print(visited)


