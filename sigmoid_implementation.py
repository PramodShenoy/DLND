import numpy as np

def sigmoid(x):
    # TODO: Implement sigmoid function
    sigm=1/(1+np.exp(-x))
    return sigm

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# TODO: Calculate the output
linear_combi=np.dot(inputs,weights)+bias
output = sigmoid(linear_combi)

print('Output:')
print(output)
