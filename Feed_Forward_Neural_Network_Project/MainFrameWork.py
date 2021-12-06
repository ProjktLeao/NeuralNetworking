import numpy as np

#Components of a neural network:

# -Layers: (check)
#   -Weights (check)
#   -Inputs (check)
#   -Neurons (check)
#   -Bias (check)
#-Activation Functions: (check)
#   -ReLU (max(0,X)) (check)
#   -Softmax (E**x normalized into %'s) (check)
#-Error Calculation (check)
#-Gradient Decent
#-BackPropagation


class network:
    class layer:
        def __init__(self, n_neurons, n_inputs) -> None:
            self.weights = 0.1 * np.random.randn(n_neurons,n_inputs)
            self.bias = 0
        
        def Forward(self, inputs, activation = "ReLU"):
            if activation == "ReLU":
                self.Output = self.Activation_ReLU(np.dot(inputs,self.weights) + self.bias)
            elif activation == "SoftMax":
                self.Output = self.Activation_Softmax(np.dot(inputs,self.weights) + self.bias)
        
        def Activation_ReLU(self,outputs):
            return np.maximum(0,outputs)
        
        def Activation_SoftMax(self,outputs):
            exp_values = np.exp(outputs)
            return exp_values/np.sum(exp_values, axis=1, keepdims= True)

    class loss:
        class mse:
            def Calculate(self, y_actual, y_pred):
                loss = 0
                n = len(y_pred)
                for i in y_pred:
                    loss += np.sqrt(y_actual[i] - y_pred[i])
                return loss/n
        class sse:
            def Calculate(self, y_actual, y_pred):
                loss = 0
                for i in y_pred:
                    loss += (y_actual[i] - y_pred[i])**2
                return loss
        class err:
            def Calculate(self, y_actual, y_pred):
                loss = 0
                for i in y_pred:
                    loss += (y_actual[i] - y_pred[i])
                return loss
    class back_propagation:
        np.gradient