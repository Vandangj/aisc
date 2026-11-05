import numpy as np
# Fuzzy Set Operations
A = np.array([0.1, 0.2, 0.4, 0.6, 1.0])
B = np.array([1.0, 0.5, 0.7, 0.3, 0.0])
a = np.maximum(A, B)
b = np.minimum(A, B)
c = 1.0 - A
d = 1.0 - B

print("A union B:", np.round(a, 2).tolist())
print("A intersection B:", np.round(b, 2).tolist())
print("Complement of A:", np.round(c, 2).tolist())
print("Complement of B:", np.round(d, 2).tolist())

print()
# Unit 10 Sum 9
A = np.array([1.0, 1.0, 0.8, 0.2, 0.1, 0.0, 0.0])
B = np.array([0.0, 0.0, 0.0, 0.5, 0.7, 0.8, 1.0])

a = A + B - A * B
b = A * B
c = np.minimum(1, A + B)
d = np.maximum(0, A + B - 1)
print("Algebraic Sum:", np.round(a, 2).tolist())
print("Algebraic Product:", np.round(b, 2).tolist())
print("Bounded Sum:", np.round(c, 2).tolist())
print("Bounded Difference:", np.round(d, 2).tolist())
print()
# Unit 11 Sum 2
A = np.array([0.5, 0.2, 0.9])
B = np.array([1.0, 0.5, 1.0])
R = np.minimum.outer(A, B)
print("Cartesian Product:")
print(R)
print()
# Unit 11 Sum 3
R = np.array([[0.1, 0.2, 0.3],
[0.4, 0.5, 0.6]])
S = np.array([[0.8, 0.1],
[0.6, 0.9],
[0.4, 1.0]])
import numpy as np
# Unit 11 Sum 3
R = np.array([[0.1, 0.2, 0.3],
[0.4, 0.5, 0.6]])

S = np.array([[0.8, 0.1],
[0.6, 0.9],
[0.4, 1.0]])
a = np.zeros((2, 2))
b = np.zeros((2, 2))
for i in range(2):
    for j in range(2):
        x = []
        for k in range(3):
            x.append(min(R[i][k], S[k][j]))
        a[i][j] = max(x)
for i in range(2):
    for j in range(2):
        x = []
        for k in range(3):
            x.append(R[i][k] * S[k][j])
        b[i][j] = max(x)
print("Max-Min Composition:")
print(a)
print("Max-Product Composition:")
print(np.round(b, 2))

// output

C:\Users\vandan>python -u "c:\Users\vandan\import csv.py"
A union B: [1.0, 0.5, 0.7, 0.6, 1.0]
A intersection B: [0.1, 0.2, 0.4, 0.3, 0.0]
Complement of A: [0.9, 0.8, 0.6, 0.4, 0.0]
Complement of B: [0.0, 0.5, 0.3, 0.7, 1.0]

Algebraic Sum: [1.0, 1.0, 0.8, 0.6, 0.73, 0.8, 1.0]
Algebraic Product: [0.0, 0.0, 0.0, 0.1, 0.07, 0.0, 0.0]
Bounded Sum: [1.0, 1.0, 0.8, 0.7, 0.8, 0.8, 1.0]
Bounded Difference: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

Cartesian Product:
[[0.5 0.5 0.5]
 [0.2 0.2 0.2]
 [0.9 0.5 0.9]]

Max-Min Composition:
[[0.3 0.3]
 [0.5 0.6]]
Max-Product Composition:
[[0.12 0.3 ]
 [0.32 0.6 ]]

C:\Users\vandan>
