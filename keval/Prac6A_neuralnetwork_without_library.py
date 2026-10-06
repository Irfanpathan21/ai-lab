# Neural Network (Perceptron for AND Gate)

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
Y  = [0, 0, 0, 1]   # AND Gate Output

w1 = 0
w2 = 0
b = 0

lr = 0.2

print("Keval Doshi")
print("53013240009")

epoch = 1

while True:
    error = 0
    print("\nEpoch", epoch)

    for i in range(4):
        z = x1[i] * w1 + x2[i] * w2 + b

        # Step Activation Function
        if z >= 0:
            y = 1
        else:
            y = 0

        print("\nInput :", x1[i], x2[i])
        print("Predicted :", y)
        print("Actual    :", Y[i])

        # Perceptron Learning Rule
        if y != Y[i]:
            w1 = w1 + lr * (Y[i] - y) * x1[i]
            w2 = w2 + lr * (Y[i] - y) * x2[i]
            b  = b  + lr * (Y[i] - y)
            error = 1

            print("Updated Parameters")
            print("w1 =", w1)
            print("w2 =", w2)
            print("b  =", b)

    if error == 0:
        break

    epoch += 1

print("\nTraining Completed")
print("Final w1 =", w1)
print("Final w2 =", w2)
print("Final b  =", b)
