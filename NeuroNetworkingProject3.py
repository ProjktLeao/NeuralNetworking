import numpy as np
from numpy.lib.function_base import gradient


X = [1,2,3,4]#inputs
y = [0,0,1]


class Hidden_Layer: #allows creation of a new layer using inputs, neurons, weights, and biases
    def __init__(self, n_inputs, n_neurons) -> None:
        self.weight = 0.1 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self):
        self.output = (np.dot(X,self.weight)) + self.biases


class Activation_ReLU: #Checks if greater than 0 and if its not the value is set to zero
    def Forward(self, inputs):
        self.output = np.maximum(0,inputs)


class Activation_SoftMax: #uses E**x to get positive outputs that are then normalized to add up to 1
    def Forward(self, inputs):
        exp_values = np.exp(inputs)
        probabilities = exp_values / sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
         
def Tuple(X,y):
    new_array = []
    for i in range(len(X)):
        new_array.append(X[i],y[i])
    return new_array

def cross_entropy(XY):
    loss = 0
    n = len(XY)
    for i in XY:
        y_actual = XY[1][i]
        y_pred = XY[0][i]
        loss += (y_actual* np.log10(y_pred)) + (1-y_actual)*np.log10(1-y_pred)
        return loss/n


def gradient_descent(X, Weights, y_target, y_pred, l_rate, bias):
    new_weights = []
    bias += l_rate*(y_pred)
    for x,w in zip(X,Weights):
        new_weight = w + l_rate*(y_target-y_pred)*x
        new_weights.append(new_weight)
    return [new_weights, bias]

error_term = cross_entropy(Tuple(X,y))


Layer1 = Hidden_Layer(4,3)#inputs are the rows and neurons are the collums in a matrix

Standard_Activation = Activation_ReLU
Final_Activation = Activation_SoftMax

gradient_term = gradient_descent(X,Layer1.weight,y,Final_Activation.output, 0.01, Layer1.biases)


def Main():
    Layer1.forward()
    Final_Activation.Forward(Layer1.output)
    print (error_term)
    Layer1.weight = gradient_term[0]
    Layer1.biases = gradient_term[1]

for iteration in  999:
    Main()