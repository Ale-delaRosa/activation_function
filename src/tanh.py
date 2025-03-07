# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the hyperbolic tangent function and its derivative
def plot_tanh():
    ''' 
    Plots the hyperbolic tangent function (tanh) and its derivative.
    The tanh function is commonly used as an activation function in neural networks.
    '''

    # Definition of the hyperbolic tangent function
    def tanh_func(x):
        return np.tanh(x)  # Returns the hyperbolic tangent of x
    
    # Derivative of the hyperbolic tangent function
    def tanh_deriv(x):
        return 1 - np.tanh(x)**2  # Formula for the derivative of tanh(x): 1 - tanh²(x)
    
    # Define the range of x values
    x = np.linspace(-5, 5, 400)  # Creates an array with 400 equally spaced values in the range [-5, 5]
    
    # Evaluate the hyperbolic tangent function at x values
    y = tanh_func(x)
    
    # Evaluate the derivative of the hyperbolic tangent function at x values
    y_deriv = tanh_deriv(x)

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the hyperbolic tangent function
    plt.plot(x, y, label='Hyperbolic Tangent (tanh x)')  
    
    # Plot the derivative of the hyperbolic tangent function with a dashed green line
    plt.plot(x, y_deriv, label='Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Hyperbolic Tangent Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_tanh()  # Calls the function to plot the hyperbolic tangent function and its derivative