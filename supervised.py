import random
import math

random.seed(42)

dataset = [
    (0.1, 0.35, 0),
    (0.8, 0.90, 1),
    (0.3, 0.40, 0),
    (0.9, 0.85, 1),
    (0.5, 0.50, 1),
    (0.2, 0.60, 0),
    (0.7, 0.30, 1),
    (0.4, 0.45, 0),
    (0.6, 0.75, 1),
    (0.1, 0.20, 0),
]

# Weights from inputs to hidden layer
v11, v21, v01 = 0.6, -0.1, 0.3
v12, v22, v02 = -0.3, 0.4, 0.5

# Weights from hidden layer to output
w1, w2, w0 = 0.4, 0.1, -0.2

alpha = 0.25
epochs = 2000

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    # Derivative of sigmoid, given its output
    return output * (1 - output)

def predict_probability(x1, x2):
    z1 = sigmoid(v11 * x1 + v21 * x2 + v01)
    z2 = sigmoid(v12 * x1 + v22 * x2 + v02)
    return sigmoid(w1 * z1 + w2 * z2 + w0)

for epoch in range(epochs):
    random.shuffle(dataset)
    total_error = 0.0

    for x1, x2, target in dataset:
        # Forward pass
        z1 = sigmoid(v11 * x1 + v21 * x2 + v01)
        z2 = sigmoid(v12 * x1 + v22 * x2 + v02)
        y = sigmoid(w1 * z1 + w2 * z2 + w0)

        # Squared-error loss and output-layer delta
        error = target - y
        total_error += error ** 2
        delta_y = error * sigmoid_derivative(y)

        # Hidden-layer deltas use the output weights before they are updated
        delta_z1 = delta_y * w1 * sigmoid_derivative(z1)
        delta_z2 = delta_y * w2 * sigmoid_derivative(z2)

        # Update output-layer weights
        w1 += alpha * delta_y * z1
        w2 += alpha * delta_y * z2
        w0 += alpha * delta_y

        # Update input-to-hidden weights
        v11 += alpha * delta_z1 * x1
        v21 += alpha * delta_z1 * x2
        v01 += alpha * delta_z1

        v12 += alpha * delta_z2 * x1
        v22 += alpha * delta_z2 * x2
        v02 += alpha * delta_z2

    mse = total_error / len(dataset)

    if epoch % 100 == 0:
        print(f"Epoch: {epoch}, MSE: {mse:.4f}")

# Evaluate each example. The dataset has been shuffled, so this prints its current order.
correct = 0

for x1, x2, target in dataset:
    probability = predict_probability(x1, x2)
    predicted_class = 1 if probability >= 0.5 else 0
    label = "pass" if predicted_class == 1 else "fail"

    print(
        f"Input: ({x1}, {x2}), Target: {target}, "
        f"Probability: {probability:.4f}, Prediction: {label}"
    )

    if predicted_class == target:
        correct += 1

accuracy = correct / len(dataset) * 100
print(f"Accuracy: {accuracy:.2f}%")

// code ends here

output :

Epoch: 0, MSE: 0.2548
Epoch: 100, MSE: 0.2081
Epoch: 200, MSE: 0.0852
Epoch: 300, MSE: 0.0484
Epoch: 400, MSE: 0.0354
Epoch: 500, MSE: 0.0285
Epoch: 600, MSE: 0.0240
Epoch: 700, MSE: 0.0207
Epoch: 800, MSE: 0.0182
Epoch: 900, MSE: 0.0161
Epoch: 1000, MSE: 0.0144
Epoch: 1100, MSE: 0.0129
Epoch: 1200, MSE: 0.0116
Epoch: 1300, MSE: 0.0105
Epoch: 1400, MSE: 0.0095
Epoch: 1500, MSE: 0.0087
Epoch: 1600, MSE: 0.0079
Epoch: 1700, MSE: 0.0073
Epoch: 1800, MSE: 0.0067
Epoch: 1900, MSE: 0.0062
Input: (0.1, 0.35), Target: 0, Probability: 0.0009, Prediction: fail
Input: (0.6, 0.75), Target: 1, Probability: 0.9938, Prediction: pass
Input: (0.1, 0.2), Target: 0, Probability: 0.0007, Prediction: fail
Input: (0.5, 0.5), Target: 1, Probability: 0.8360, Prediction: pass
Input: (0.2, 0.6), Target: 0, Probability: 0.0047, Prediction: fail
Input: (0.9, 0.85), Target: 1, Probability: 0.9994, Prediction: pass
Input: (0.8, 0.9), Target: 1, Probability: 0.9992, Prediction: pass
Input: (0.3, 0.4), Target: 0, Probability: 0.0122, Prediction: fail
Input: (0.7, 0.3), Target: 1, Probability: 0.9936, Prediction: pass
Input: (0.4, 0.45), Target: 0, Probability: 0.1633, Prediction: fail
Accuracy: 100.00%
