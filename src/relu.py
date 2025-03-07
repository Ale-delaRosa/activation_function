# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the ReLU function and its derivative
def plot_relu():
    ''' 
    Plots the ReLU (Rectified Linear Unit) function and its derivative.
    ReLU is widely used as an activation function in deep learning models.
    '''
   
    # Definition of the ReLU (Rectified Linear Unit) function
    def relu(x):
        return np.maximum(0, x)  # Returns x if x > 0, and 0 if x ≤ 0
    
    # Derivative of the ReLU function
    def relu_deriv(x):
        return np.where(x > 0, 1, 0)  # The derivative is 1 if x > 0, and 0 if x ≤ 0
    
    # Define the range of x values
    x = np.linspace(-10, 10, 400)  # Creates an array with 400 equally spaced values in the range [-10, 10]
    
    # Evaluate the ReLU function at x values
    y = relu(x)
    
    # Evaluate the derivative of the ReLU function at x values
    y_deriv = relu_deriv(x)

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the ReLU function
    plt.plot(x, y, label='ReLU Function')  
    
    # Plot the derivative of the ReLU function with a dashed green line
    plt.plot(x, y_deriv, label='ReLU Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('ReLU Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_relu()  # Calls the function to plot the ReLU function and its derivative