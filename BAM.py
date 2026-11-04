import numpy as np
x=np.array([[-1,1,1,1]])
xtranspose = x.T
w=xtranspose @ x 
y=x@w

def activation_function(y):
    return np.where(y > 0,1,np.where(y < 0, -1, 0))

print(activation_function(y))

x1=np.array([[0,1,1,1]])
y1=x1 @ w
print("Test Input 1 Output:", activation_function(y1))
# test input 2
x2=np.array([[-1,1,0,1]])
y2=x2 @ w
print("Test Input 2 Output:", activation_function(y2))
# test input 4
x4=np.array([[0,0,1,1]])
y4=x4 @ w
print("Test Input 4 Output:", activation_function(y4))
# test input 5
x5=np.array([[-1,-1,-1,1]])
y5=x5 @ w
print("Test Input 5 Output:", activation_function(y5)) 
# test input 3
x3=np.array([[-1,-1,1,1]])
y3=x3 @ w
print("Test Input 3 Output:", activation_function(y3)) 

# heterogenous memory
s=np.array([[1,0,0,0],[1,1,0,0],[0,0,0,1],[0,0,1,1]])
t=np.array([[0,1],[0,1],[1,0],[1,0]])
w1 = s.T @ t
print("Heteroassociative Weight Matrix w1")
print(w1)

def activation_hetero(y):
    return np.where(y > 0, 1, 0)

x6=np.array([[1,1,0,0]])
y_hetero=x6 @ w1

print("Heteroassociative Output x6:", activation_hetero(y_hetero))
E = np.array([[1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1]])
target_E = np.array([[-1,1]])

F = np.array([[1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1]])
target_F = np.array([[1,1]])

w_bam = (E.T @ target_E) + (F.T @ target_F) 

def activation_bam(y):
 return np.where(y > 0, 1, -1)

yin_E = E @ w_bam
print("BAM Output E:", activation_bam(yin_E))

yin_F = F @ w_bam
print(yin_E,yin_F)
print("BAM Output F:", activation_bam(yin_F))

#short cut just remember these
''' xtranspose = x.T
    w=xtranspose @ x 
    y=x@w 
    activation_function(y)'''

/// code ends here 

output:
[[-1  1  1  1]]
Test Input 1 Output: [[-1  1  1  1]]
Test Input 2 Output: [[-1  1  1  1]]
Test Input 4 Output: [[-1  1  1  1]]
Test Input 5 Output: [[0 0 0 0]]
Test Input 3 Output: [[-1  1  1  1]]
Heteroassociative Weight Matrix w1
[[0 2]
 [0 1]
 [1 0]
 [2 0]]
Heteroassociative Output x6: [[0 1]]
BAM Output E: [[-1  1]]
[[-12  18]] [[12 18]]
BAM Output F: [[1 1]]
