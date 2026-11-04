x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]
thetas =[0, 1, 2] 

def neuron(x1,x2,w1,w2):
    y=[]
    for i in range(len(x1)):
        y.append(w1[i]*x1[i] + w2[i]*x2[i])
    return y

neural_output = neuron(x1, x2, w1, w2)  

print(f"Y in: {neural_output}")

for theta in thetas:
    print(f"Threshold: {theta}")
    final=[]
    for output in neural_output:
        if output >= theta:
            final.append(1)
        else:
            final.append(0)
    print(f"Final Output: {final}")
    final=[]

not_gate=[]
for output in neural_output:
    if output < 1:
        not_gate.append(1)
    else:
        not_gate.append(0)
print(f"NOT Gate Output: {not_gate}")


def halfadder(x1, x2):
    sum_output = []
    carry_output = []
    for i in range(len(x1)):
        sum_output.append(x1[i] ^ x2[i])  # XOR operation for sum
        carry_output.append(x1[i] & x2[i])  # AND operation for carry
    return sum_output, carry_output

half_sum, half_carry = halfadder(x1, x2)
print(f"Half Adder Sum Output: {half_sum}")
print(f"Half Adder Carry Output: {half_carry}")

a=[0, 0, 1, 1] 
b=[0, 1, 0, 1]
c=[0, 1, 0, 1]

def fulladder(a, b,c):
    sum_output = []
    carry_output = []
    for i in range(len(a)):
        sum_bit = a[i] ^ b[i] ^ c[i]  # XOR operation for sum
        carry_bit = (a[i] & b[i]) | (b[i] & c[i]) | (a[i] & c[i])  # Carry calculation
        sum_output.append(sum_bit)
        carry_output.append(carry_bit)
    return sum_output, carry_output

full_sum, full_carry = fulladder(a, b, c)
print(f"Full Adder Sum Output: {full_sum}")
print(f"Full Adder Carry Output: {full_carry}")

/// code ends here 

output 
Y in: [0, 1, 1, 2]
Threshold: 0
Final Output: [1, 1, 1, 1]
Threshold: 1
Final Output: [0, 1, 1, 1]
Threshold: 2
Final Output: [0, 0, 0, 1]
NOT Gate Output: [1, 0, 0, 0]
Half Adder Sum Output: [0, 1, 1, 0]
Half Adder Carry Output: [0, 0, 0, 1]
Full Adder Sum Output: [0, 0, 1, 1]
Full Adder Carry Output: [0, 1, 0, 1]
