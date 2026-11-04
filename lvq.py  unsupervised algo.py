w = [(0.3, 0.5), (0.2, 0.6), (0.1, 0.7), (0.8, 0.9), (0.4,0.2)]
alpha = 0.2
input_vector = [0.2, 0.4]
d = [] 

for i in range(len(w)):
    distance = ((w[i][0] - input_vector[0]) ** 2 + (w[i][1] - input_vector[1]) ** 2) ** 0.5
    d.append(distance)

winner_index = d.index(min(d))
w[winner_index] = (round(w[winner_index][0] + alpha * (input_vector[0] - w[winner_index][0]), 1),
                  round(w[winner_index][1] + alpha * (input_vector[1] - w[winner_index][1]), 1))

print("Updated weight vector:", w)

w1=[0,0,1,1]
w2=[1,0,0,0]
a=0.1
input=[[0,0,0,1], [1,1,0,0], [0,1,1,0]]
target=[2,1,1]

for i in range(len(target)):
    d1=0
    d2=0
    for j in range(len(w1)):
        d1+= (w1[j] - input[i][j]) ** 2
        d2+= (w2[j] - input[i][j]) ** 2

    if d1 < d2:
        weights = w1
        winner_idx = 1
    else:
        weights = w2
        winner_idx = 2

    if winner_idx == target[i]:
        for k in range(len(weights)):
            weights[k] += round(a * (input[i][k] - weights[k]), 1)
    else:
        for k in range(len(weights)):
            weights[k] -= round(a * (input[i][k] - weights[k]), 1)

    print(f"input: {input[i]},winner: {winner_idx}, target: {target[i]}, updated weights: {weights} ")

// code ends here 

Updated weight vector: [(0.3, 0.5), (0.2, 0.6), (0.1, 0.7), (0.8, 0.9), (0.4, 0.2)]
input: [0, 0, 0, 1], target: 2, updated weights: [0.0, 0.0, 1.1, 1.0] 
input: [1, 1, 0, 0], target: 1, updated weights: [1.0, -0.1, 0.0, 0.0] 
input: [0, 1, 1, 0], target: 1, updated weights: [1.1, -0.2, -0.1, 0.0] 
