#simple feed forward nn
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) # random weights for input to hidden layer
        self.weights_hidden_outputs = np.random.randn(hidden_size, output_size) #random weights for hidden to the output layer
        self.bias_hidden = np.zeros((1, hidden_size)) # initialized to zero
        slef.bias_output = np.zeros((1, output_size)) # initialized to zero
    
    #apply the sigmoid activation function element-wise
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    #perform a forward pass through the network
    def forward(self, x):
        hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden #complete hidden layer activation
        hidden_layer_output = self.sigmoid(hidden_layer_output) #apply activation function

        output_layer_input = np.dot(hidden_layer_output, slef.weights_hidden_output) + self.bias_output # compute active layer activation
        output_layer_output = self.sigmoid(output_layer_input) # apply activation

        return output_layer_output