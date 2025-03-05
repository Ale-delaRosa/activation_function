# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the sigmoid function and its derivative
def plot_sigmoid():
   
    # Definition of the sigmoid function
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))  # Sigmoid function formula

    # Derivative of the sigmoid function
    def sigmoid_deriv(x):
        s = sigmoid(x)  # First, compute the sigmoid
        return s * (1 - s)  # Sigmoid derivative formula: f'(x) = f(x) * (1 - f(x))

    # Define the range of x values
    x = np.linspace(-10, 10, 400)  # Creates an array with 400 equally spaced values in the range [-10, 10]
    
    # Evaluate the sigmoid function at x values
    y = sigmoid(x)
    
    # Evaluate the derivative of the sigmoid function at x values
    y_deriv = sigmoid_deriv(x)

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the sigmoid function
    plt.plot(x, y, label='Sigmoid Function')  
    
    # Plot the derivative of the sigmoid function with a dashed green line
    plt.plot(x, y_deriv, label='Sigmoid Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Sigmoid Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_sigmoid()  # Calls the function to plot the sigmoid function and its derivative