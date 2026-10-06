# AI Lab Practical Exam - Complete Viva Questions & Answers Guide 🎓

> **Subject:** Artificial Intelligence Lab (5th Semester)  
> **Coverage:** All 10 Practicals (Core Concepts, Complexities, Code Quirks, Examiner Traps & Comparisons)  
> **Language:** English with easy-to-understand explanations & Hinglish intuition.

---

## 📌 Quick Summary Table (Examiner's Favorite Reference)

| Practical | Algorithm / Topic | Data Structure | Time Complexity | Space Complexity | Search Type |
|---|---|---|---|---|---|
| **Prac 1** | Depth First Search (DFS) | **Stack** (or Recursion) | $O(V + E)$ | $O(V)$ | Uninformed (Blind) |
| **Prac 2** | Breadth First Search (BFS) | **Queue** (FIFO) | $O(V + E)$ | $O(V)$ | Uninformed (Blind) |
| **Prac 3** | Water Jug Problem | **Queue** (BFS on States) | $O(X \times Y)$ | $O(X \times Y)$ | State-Space Search |
| **Prac 4** | N-Queens Problem | **2D Array / 1D Array** | $O(N!)$ | $O(N)$ (recursion stack) | Backtracking (CSP) |
| **Prac 5** | Minimax Algorithm | **Game Tree** (DFS recursion) | $O(b^m)$ | $O(b \times m)$ | Adversarial Search |
| **Prac 6A** | Perceptron (Without Lib) | **Lists / Arrays** (Weights, Bias) | $O(\text{epochs} \times N)$ | $O(1)$ | Supervised Learning |
| **Prac 6B** | MLP (Scikit-Learn) | **Matrix Tensors** (MLPClassifier) | Depends on layers/epochs | $O(W)$ (Weights) | Supervised Deep Learning |
| **Prac 7** | Greedy Best-First Search | **Priority Queue / Sorted List** | $O(b^m)$ worst case | $O(b^m)$ | Informed ($f = h$) |
| **Prac 8** | A* Search Algorithm | **Priority Queue / Dicts** | $O(b^d)$ | $O(b^d)$ | Informed ($f = g + h$) |
| **Prac 9** | AIML Chatbot | **AIML XML Tree / Trie** | $O(\text{Pattern Length})$ | $O(\text{Vocabulary})$ | Rule-Based NLP / KB |

---

## 🌟 General AI Viva Questions (Foundational)

### Q1. What is the difference between Informed and Uninformed Search?
- **Uninformed (Blind) Search:** The search algorithm only knows the start state, goal state, and available actions. It has **no clue** how close a node is to the goal.
  - *Examples:* BFS, DFS, Uniform Cost Search.
- **Informed (Heuristic) Search:** Uses domain knowledge or an evaluation function $h(n)$ (heuristic) to estimate which path is closer to the goal, making the search significantly faster.
  - *Examples:* Greedy Best-First Search, A* Search.

### Q2. What is State-Space Search?
A problem formulation in AI where:
1. **Initial State:** Where you start (e.g., `(0, 0)` in Water Jug).
2. **Actions / Operators:** Valid legal moves (e.g., Fill Jug 1, Pour Jug 1 to 2).
3. **Goal State:** The target outcome (e.g., exactly 2 liters in a jug).
4. **Path Cost:** Numerical cost associated with the solution path.

### Q3. What is Completeness and Optimality in Search Algorithms?
- **Completeness:** Is the algorithm guaranteed to find a solution if one exists?
- **Optimality:** Does the algorithm guarantee finding the solution with the lowest path cost?

---

## 🟢 Practical 1: Depth First Search (DFS)

### Q1. What is DFS and how does it traverse a graph?
- **Answer:** DFS explores as deep as possible along each branch before backtracking. It starts at the root/source node and dives down until it hits a dead end or visited node, then backtracks to explore unexplored sibling branches.

### Q2. Which data structure is used in DFS?
- **Answer:** **Stack** (Last-In, First-Out - LIFO). In recursive code, the internal **Call Stack** of the language is used.

### Q3. Why do we maintain a `visited` list? What happens if you omit it?
- **Answer:** To prevent infinite loops in cyclic graphs. If a graph has a cycle (e.g., $A \leftrightarrow B$) and there is no `visited` set, the recursion will bounce infinitely between $A$ and $B$, causing a `RecursionError: maximum recursion depth exceeded`.

### Q4. Is DFS complete and optimal?
- **Answer:**
  - **Completeness:** **No**, in infinite-depth state spaces or graphs with cycles (without cycle detection). **Yes**, for finite acyclic state spaces.
  - **Optimality:** **No**. DFS returns the *first* path it encounters; it does not guarantee the shortest path.

### Q5. What is the Time and Space Complexity of DFS?
- **Time Complexity:** $O(V + E)$ (using adjacency list), where $V$ is vertices and $E$ is edges. (In trees: $O(b^m)$, where $b$ is branching factor and $m$ is max depth).
- **Space Complexity:** $O(V)$ (or $O(b \times m)$ in trees), which is its major advantage—it only stores nodes along the current path.

---

## 🟢 Practical 2: Breadth First Search (BFS)

### Q1. What is BFS and how does it traverse a graph?
- **Answer:** BFS explores the graph **level by level**. It visits all immediate neighbors (distance 1) before moving to neighbors of neighbors (distance 2).

### Q2. Which data structure is used in BFS?
- **Answer:** **Queue** (First-In, First-Out - FIFO).

### Q3. Is BFS complete and optimal?
- **Answer:**
  - **Completeness:** **Yes**, if the branching factor $b$ is finite.
  - **Optimality:** **Yes**, if all edge costs are uniform/equal (it finds the path with the minimum number of steps). If edge costs vary, Uniform Cost Search (Dijkstra) is required.

### Q4. What is the main drawback/bottleneck of BFS compared to DFS?
- **Answer:** **High Memory Consumption (Space Complexity)**. BFS stores all nodes of the current frontier in memory: $O(b^d)$ where $d$ is depth. For large search trees, BFS runs out of RAM long before it runs out of execution time.

### Q5. Difference between BFS and DFS (Classic Examiner Comparison):
| Property | BFS | DFS |
|---|---|---|
| **Data Structure** | Queue (FIFO) | Stack (LIFO / Recursion) |
| **Strategy** | Level-by-level | Branch-by-branch (depth-first) |
| **Shortest Path** | Yes (for unweighted graphs) | No |
| **Space Consumption** | High ($O(b^d)$) | Low ($O(b \times m)$) |
| **Infinite Path Trap** | Immune | Can get trapped in infinite paths |

---

## 🟢 Practical 3: Water Jug Problem

### Q1. What is the AI concept behind the Water Jug problem?
- **Answer:** It is a classic **State-Space Search Problem**. The problem is modeled as state transitions: $(x, y) \rightarrow (x', y')$, where $x$ and $y$ are the current volumes in Jug 1 and Jug 2.

### Q2. What algorithm is used to solve the Water Jug problem?
- **Answer:** **Breadth-First Search (BFS)** is used to explore states level-by-level. This guarantees finding the solution with the **minimum number of pouring steps**.

### Q3. What are the legal operations / production rules in Water Jug?
There are 6 possible legal actions from any state $(x, y)$:
1. **Fill Jug 1:** $(J_1, y)$
2. **Fill Jug 2:** $(x, J_2)$
3. **Empty Jug 1:** $(0, y)$
4. **Empty Jug 2:** $(x, 0)$
5. **Pour Jug 1 $\rightarrow$ Jug 2:** until Jug 2 is full or Jug 1 is empty.
6. **Pour Jug 2 $\rightarrow$ Jug 1:** until Jug 1 is full or Jug 2 is empty.

### Q4. When is a Water Jug problem solvable (Mathematical condition)?
- **Answer:** A target amount $d$ can be measured using jugs of capacity $X$ and $Y$ if and only if:
  1. $d \le \max(X, Y)$
  2. $d$ is a multiple of $\gcd(X, Y)$ (Bézout's identity).
  *Example:* Jugs of 4L and 2L ($\gcd=2$) cannot measure 3L!

### Q5. Why is state tuple `(x, y)` stored in `visited`?
- **Answer:** Because pouring back and forth creates cyclic loops (e.g., $(0,0) \rightarrow (4,0) \rightarrow (0,0)$). Storing visited tuples prevents infinite cycles.

---

## 🟢 Practical 4: N-Queens Problem

### Q1. What is the N-Queens problem?
- **Answer:** The goal is to place $N$ non-attacking chess queens on an $N \times N$ chessboard such that no two queens share the same **row**, **column**, or **diagonal**.

### Q2. Which AI technique is used to solve N-Queens?
- **Answer:** **Backtracking** (a systematic depth-first search for Constraint Satisfaction Problems - CSP).

### Q3. What is Backtracking?
- **Answer:** Backtracking builds candidates for the solution incrementally. As soon as it determines that the current candidate cannot lead to a valid valid solution, it **abandons (prunes)** that candidate and steps back (*backtracks*) to the previous decision point.
  - In code: `place_queen() -> if solve(next): return True -> remove_queen() (backtrack)`

### Q4. How do you check if a queen placement is safe?
- **Answer:** Since we place queens column-by-column from left to right:
  1. Check **left row** horizontally: `board[row][i] == 1`
  2. Check **upper-left diagonal**: `row - 1, col - 1`
  3. Check **lower-left diagonal**: `row + 1, col - 1`
  *(Note: We don't need to check right-side columns because queens haven't been placed there yet!)*

### Q5. For which values of $N$ does a solution NOT exist?
- **Answer:**
  - $N = 1$: Trivial solution (1 queen on $1 \times 1$).
  - $N = 2$ and $N = 3$: **No solution exists**.
  - $N \ge 4$: Always has at least one solution (e.g., $N=4$ has 2 distinct solutions).

---

## 🟢 Practical 5: Minimax Algorithm (Game Playing)

### Q1. What is the Minimax algorithm?
- **Answer:** Minimax is a decision-making algorithm for **two-player, zero-sum, perfect information games** (e.g., Tic-Tac-Toe, Chess).
  - One player is **MAX** (tries to maximize the score / AI).
  - The other player is **MIN** (tries to minimize the score / Opponent).

### Q2. What does "Zero-Sum Game" mean?
- **Answer:** One player's gain is exactly equal to the other player's loss ($+1 + (-1) = 0$). There is no win-win scenario.

### Q3. How does the recursive Minimax function evaluate game states?
- **Answer:**
  - **Base Case (Terminal State):**
    - If AI wins $\rightarrow$ Return $+1$ (or $+10$)
    - If Opponent wins $\rightarrow$ Return $-1$ (or $-10$)
    - If Draw $\rightarrow$ Return $0$
  - **MAX turn:** Return $\max(\text{Minimax}(\text{child moves}))$
  - **MIN turn:** Return $\min(\text{Minimax}(\text{child moves}))$

### Q4. What is the time complexity of Minimax and how can it be optimized?
- **Answer:**
  - Time Complexity: $O(b^m)$ ($b$ = branching factor, $m$ = maximum depth).
  - Optimization: **Alpha-Beta Pruning**. It prunes branches that cannot possibly influence the final decision, reducing effective complexity to $O(b^{m/2})$.

### Q5. What are $\alpha$ (Alpha) and $\beta$ (Beta) in Alpha-Beta pruning?
- **Answer:**
  - $\alpha$: Best (highest) value MAX can guarantee so far.
  - $\beta$: Best (lowest) value MIN can guarantee so far.
  - Pruning condition: Whenever $\alpha \ge \beta$, stop evaluating remaining siblings.

---

## 🟢 Practical 6A: Perceptron (Without Library)

### Q1. What is a Perceptron?
- **Answer:** A Perceptron is the simplest type of artificial neural network (single-layer binary classifier invented by Frank Rosenblatt in 1958). It takes numerical inputs, computes a weighted sum, adds a bias, and passes it through an activation function to output 0 or 1.

### Q2. What is the mathematical equation of a Perceptron?
$$\hat{y} = f(z) = f\left(\sum_{i=1}^n w_i x_i + b\right)$$
Where:
- $x_i$ = Inputs
- $w_i$ = Weights
- $b$ = Bias
- $f$ = Activation function (Step function: returns $1$ if $z \ge 0$, else $0$).

### Q3. What is the Perceptron Weight Update Rule?
$$w_i = w_i + \alpha \times (y - \hat{y}) \times x_i$$
$$b = b + \alpha \times (y - \hat{y})$$
Where:
- $\alpha$ is the **Learning Rate** (step size).
- $(y - \hat{y})$ is the **Error** (Target $-$ Predicted).
- If prediction is correct ($y - \hat{y} = 0$), weights do NOT change!

### Q4. What is Linear Separability and the XOR Limitation?
- **Answer:** A dataset is **linearly separable** if classes can be separated by a single straight line (hyperplane).
  - Single-layer Perceptrons can solve **AND** and **OR** gates.
  - They **CANNOT solve XOR** gate because XOR is non-linearly separable (proven by Minsky & Papert in 1969).
  - Solution to XOR: Multi-Layer Perceptron (MLP) with non-linear activation functions.

### Q5. What is an Epoch?
- **Answer:** One complete pass through the entire training dataset during training.

---

## 🟢 Practical 6B: Neural Network with Library (Scikit-Learn MLPClassifier)

### Q1. What is an MLP (Multi-Layer Perceptron)?
- **Answer:** A feedforward artificial neural network consisting of at least 3 layers:
  1. **Input Layer**
  2. One or more **Hidden Layers** (with non-linear activation functions)
  3. **Output Layer**
  It can learn non-linear decision boundaries and solve complex problems like XOR.

### Q2. What is Backpropagation?
- **Answer:** The primary learning algorithm for MLPs. It calculates the gradient of the loss function with respect to each weight using the **Chain Rule of calculus**, propagating errors backward from the output layer to the input layer to update weights.

### Q3. Explain key parameters of `MLPClassifier`:
- `hidden_layer_sizes=(4, 2)`: Defines the architecture (e.g., 1st hidden layer has 4 neurons, 2nd has 2 neurons).
- `activation='relu'` or `'logistic'`: The non-linear activation function used in hidden neurons.
- `max_iter=1000`: Maximum number of epochs.
- `learning_rate_init=0.01`: Initial step size for gradient descent weight updates.

### Q4. Why do neural networks require non-linear activation functions?
- **Answer:** If all activation functions were linear, stacking multiple layers would still result in a simple linear transformation ($W_2(W_1 x) = W_{combined} x$). Non-linear activations enable neural networks to be **Universal Function Approximators**.

---

## 🟢 Practical 7: Greedy Best-First Search (GBFS)

### Q1. What is Greedy Best-First Search?
- **Answer:** An informed (heuristic) search algorithm that selects the next node to expand strictly based on the heuristic value:
  $$f(n) = h(n)$$
  It always chooses the node that appears closest to the goal, ignoring the cost already spent to reach that node.

### Q2. What is a Heuristic Function $h(n)$?
- **Answer:** A problem-specific rule-of-thumb estimate of the cost from node $n$ to the goal.
  - In road networks: Straight-line Euclidean distance to the goal.
  - In 8-Puzzle: Manhattan distance or number of misplaced tiles.
  - At the goal node: $h(\text{Goal}) = 0$.

### Q3. Is Greedy BFS complete and optimal?
- **Answer:**
  - **Completeness:** **No**, it can get stuck in infinite loops in cyclic graphs unless visited nodes are tracked.
  - **Optimality:** **No**, it is not optimal. Because it ignores path cost $g(n)$, it can choose a path that looks superficially close to the goal but actually has an enormous overall path cost.

### Q4. How does GBFS choose which node to expand in code?
- **Answer:**
  `next_node = min(open_list, key=lambda node: heuristic[node])`

---

## 🟢 Practical 8: A* (A-Star) Search Algorithm

### Q1. What is the A* Search Algorithm and its evaluation function?
- **Answer:** A* is an informed search algorithm that evaluates nodes combining actual cost and heuristic estimate:
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: The exact cost incurred from the start node to current node $n$.
  - $h(n)$: The estimated heuristic cost from node $n$ to the goal.
  - $f(n)$: Total estimated cost of the cheapest solution passing through $n$.

### Q2. When is A* guaranteed to be Optimal?
- **Answer:**
  1. For Tree Search: Heuristic $h(n)$ must be **Admissible**.
  2. For Graph Search: Heuristic $h(n)$ must be **Consistent (Monotonic)**.

### Q3. What is an Admissible Heuristic?
- **Answer:** A heuristic is admissible if it **never overestimates** the actual true cost to reach the goal:
  $$h(n) \le h^*(n) \quad \text{for all } n$$
  *(It is optimistic).*
  *Example:* Straight-line aerial distance is always $\le$ actual road distance.

### Q4. What is a Consistent (Monotonic) Heuristic?
- **Answer:** For every node $n$ and every successor $n'$ generated by action with cost $c(n, n')$:
  $$h(n) \le c(n, n') + h(n')$$
  *(Satisfies Triangle Inequality).* Consistency implies admissibility.

### Q5. What happens to A* if $h(n) = 0$ for all nodes?
- **Answer:**
  $$f(n) = g(n) + 0 = g(n)$$
  **A* becomes Dijkstra's Algorithm (Uniform Cost Search)!**

### Q6. Difference between Greedy BFS and A*:
| Feature | Greedy Best-First Search | A* Search |
|---|---|---|
| **Evaluation Function** | $f(n) = h(n)$ | $f(n) = g(n) + h(n)$ |
| **Path Cost Considered?** | No ($g(n)$ ignored) | Yes ($g(n)$ included) |
| **Optimality** | Not optimal | Optimal (if $h$ is admissible) |
| **Expansion Criterion** | "What looks closest right now" | "What has lowest overall estimated path cost" |

---

## 🟢 Practical 9: AIML Chatbot

### Q1. What is AIML?
- **Answer:** **Artificial Intelligence Markup Language** is an XML-based language designed by Dr. Richard Wallace (creator of A.L.I.C.E.) for building conversational rule-based software agents and chatbots.

### Q2. What are the core tags in an AIML file?
1. `<aiml>`: Root tag enclosing the knowledge base.
2. `<category>`: The basic unit of knowledge. Contains exactly one `<pattern>` and one `<template>`.
3. `<pattern>`: The user's input phrase to match (usually in UPPERCASE).
4. `<template>`: The chatbot's reply/response.
5. `<srai>`: Symbolic Reduction / Synonym mapping (redirects one pattern to another).
6. `<star/>`: Wildcard replacement; captures whatever matched `*` in the pattern.

### Q3. How does AIML pattern matching work?
- **Answer:** It uses normalized text matching based on a tree structure (called the **Graphmaster**). User input is capitalized, stripped of punctuation, and matched against stored patterns.

### Q4. In Python, why was `time.clock = time.perf_counter` added in code?
- **Answer:** In Python 3.8+, the legacy function `time.clock()` was completely removed in favor of `time.perf_counter()`. Because the third-party `aiml` library was written for older Python versions and internally calls `time.clock()`, assigning `time.clock = time.perf_counter` prevents an `AttributeError: module 'time' has no attribute 'clock'`.

### Q5. What is the fallback mechanism if user input does not match any AIML rule?
- **Answer:** In Python:
  ```python
  response = bot.respond(user_input)
  if not response:
      response = "Sorry, I only have info on college timings, courses, and admissions."
  ```
  In AIML itself, a wildcard pattern `<pattern>*</pattern>` can serve as a catch-all fallback category.

---

## ⚡ Rapid-Fire Cheat Sheet for Exam Hall

1. **Which search is used in Water Jug?** $\rightarrow$ **BFS** (to find minimum pouring steps).
2. **Which algorithmic paradigm is N-Queens?** $\rightarrow$ **Backtracking** (Recursive Depth-First CSP).
3. **Can 1-Layer Perceptron solve XOR?** $\rightarrow$ **No**, because XOR is not linearly separable.
4. **Formula for A*?** $\rightarrow$ $f(n) = g(n) + h(n)$.
5. **Formula for Greedy BFS?** $\rightarrow$ $f(n) = h(n)$.
6. **Data structure for BFS?** $\rightarrow$ **Queue (FIFO)**.
7. **Data structure for DFS?** $\rightarrow$ **Stack (LIFO)**.
8. **What does AIML stand for?** $\rightarrow$ **Artificial Intelligence Markup Language**.
9. **Who is MAX and who is MIN in Tic-Tac-Toe?** $\rightarrow$ MAX is AI (+1), MIN is Human (-1).
10. **What is an admissible heuristic?** $\rightarrow$ A heuristic that never overestimates the true cost to reach the goal.
