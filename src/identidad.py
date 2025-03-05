# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the identity function and its derivative
def plot_identity():

    # Definition of the identity function (f(x) = x)
    def identity(x):
        return x  # The identity function simply returns the same input value
    
    # Derivative of the identity function (f'(x) = 1 for all x)
    def identity_deriv(x):
        return np.ones_like(x)  # The derivative is always 1, so an array filled with ones is used
    
    # Define the range of x values
    x = np.linspace(-10, 10, 400)  # Creates an array with 400 equally spaced values in the range [-10, 10]
    
    # Evaluate the identity function at x values
    y = identity(x)
    
    # Evaluate the derivative of the identity function at x values
    y_deriv = identity_deriv(x)
    
    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the identity function
    plt.plot(x, y, label='Identity Function')  
    
    # Plot the derivative of the identity function with a dashed green line
    plt.plot(x, y_deriv, label='Derivative (Constant 1)', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Identity Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_identity()  # Calls the function to plot the identity function and its derivative