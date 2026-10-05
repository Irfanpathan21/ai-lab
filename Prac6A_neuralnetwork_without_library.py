# =====================================================================
# PRACTICAL 6A: PERCEPTRON (NEURAL NETWORK WITHOUT LIBRARY)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Single-Layer Perceptron Learning Rule
# FORMULAS TO REMEMBER:
#   1. Linear Output:     z = (x1 * w1) + (x2 * w2) + b
#   2. Activation (Step): pred = 1 if z >= 0 else 0
#   3. Error:             error = target - pred
#   4. Weight Update:     w = w + lr * error * x,   b = b + lr * error
#
# EXAM ADAPTATION GUIDE:
#   - To train OR Gate:   Change Y = [0, 1, 1, 1]
#   - To train NAND Gate: Change Y = [1, 1, 1, 0]
#   - To train NOR Gate:  Change Y = [1, 0, 0, 0]
# =====================================================================

# 1. Dataset (AND Gate Truth Table)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
Y = [0, 0, 0, 1]  # Target outputs for AND Gate

# 2. Parameters
w1, w2, b = 0.0, 0.0, 0.0
lr = 0.2

# 3. Training Loop (Step-by-Step Epoch Progression)
for epoch in range(1, 20):
    total_error = 0
    print(f"\n--- Epoch {epoch} ---")

    for (x1, x2), target in zip(X, Y):
        z = (x1 * w1) + (x2 * w2) + b
        pred = 1 if z >= 0 else 0
        error = target - pred

        print(f"Input: ({x1}, {x2}) | Target: {target} | Pred: {pred} | Err: {error}")

        if error != 0:
            w1 += lr * error * x1
            w2 += lr * error * x2
            b  += lr * error
            total_error += abs(error)
            print(f"  -> Updated: w1={round(w1,2)}, w2={round(w2,2)}, b={round(b,2)}")

    if total_error == 0:
        print(f"\nTraining Converged at Epoch {epoch}!")
        break

# 4. Final Results & Testing
print(f"\nLearned: w1={round(w1, 2)}, w2={round(w2, 2)}, bias={round(b, 2)}")
print("Predictions on AND Gate:")
for x1, x2 in X:
    z = (x1 * w1) + (x2 * w2) + b
    print(f"  Input: ({x1}, {x2}) -> Output: {1 if z >= 0 else 0}")
