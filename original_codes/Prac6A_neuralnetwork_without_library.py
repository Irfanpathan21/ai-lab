# =====================================================================
# PRACTICAL 6A: PERCEPTRON (NEURAL NETWORK WITHOUT LIBRARY)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Problem: AND Gate ko bina kisi library ke single neuron (Perceptron)
#          se train karke weights aur bias nikaalna.
# =====================================================================

# Q1. STATE / DATA REPRESENTATION: Input aur Target output kaisa dikhta hai?
# AND Gate Truth Table:
# X1  X2  |  Target Y
#  0   0  |    0
#  0   1  |    0
#  1   0  |    0
#  1   1  |    1
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
Y = [0, 0, 0, 1]  # Target outputs

# Initial Weights, Bias, aur Learning Rate (lr)
w1 = 0.0
w2 = 0.0
b = 0.0
lr = 0.2  # Learning Rate: kitna tezi se weights update honge

epoch = 1

# Training Loop
while True:
    total_errors = 0
    print(f"\n--- Epoch {epoch} ---")

    for i in range(len(X)):
        x1, x2 = X[i]
        target = Y[i]

        # Q2. FORWARD PASS / PREDICTION: Neuron output kaise calculate karta hai?
        # Step 1: Weighted sum (z = x1*w1 + x2*w2 + b)
        z = (x1 * w1) + (x2 * w2) + b

        # Step 2: Step Activation Function (Agar z >= 0 to 1, warna 0)
        y_pred = 1 if z >= 0 else 0

        # Error check: Actual minus Predicted
        error = target - y_pred

        print(f"Input: ({x1}, {x2}) | Target: {target} | Predicted: {y_pred} | Error: {error}")

        # Q4. WEIGHT UPDATE RULE: Agar galti hui to weights kaise sudharein?
        # Formula: w_new = w_old + lr * error * input
        #          b_new = b_old + lr * error
        if error != 0:
            w1 += lr * error * x1
            w2 += lr * error * x2
            b += lr * error
            total_errors += 1
            print(f"  -> Updated: w1={round(w1,2)}, w2={round(w2,2)}, b={round(b,2)}")

    # Q3. STOPPING CONDITION: Kab training roki jaye?
    # Jab poore table me ek bhi galti (total_errors == 0) na ho!
    if total_errors == 0:
        print(f"\nTraining Successful! No errors in Epoch {epoch}.")
        break

    epoch += 1

print("\nFinal Learned Parameters:")
print(f"Weight 1 (w1) = {round(w1, 2)}")
print(f"Weight 2 (w2) = {round(w2, 2)}")
print(f"Bias (b)      = {round(b, 2)}")

# Testing the Trained AND Gate on all combinations
print("\n--- Testing the Trained AND Gate ---")
for x1, x2 in X:
    z = (x1 * w1) + (x2 * w2) + b
    pred = 1 if z >= 0 else 0
    print(f"Input: ({x1}, {x2}) -> Output: {pred}")
