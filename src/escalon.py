# Import necessary libraries
import numpy as np  # Library for mathematical operations and array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Define the function that plots the step function (Heaviside) and its approximate derivative
def plot_step_function():
    """
    This function plots the Heaviside step function and its approximate derivative.
    The derivative is approximated as a zero function except for a discontinuity at x = 0.
    """
    
    # Define the step function (Heaviside)
    def step_function(x):
        return np.where(x < 0, 0, 1)  # Returns 0 if x < 0, and 1 if x >= 0
    
    # Define the range of values for x
    x = np.linspace(-10, 10, 400)  # Creates an array of 400 evenly spaced values in the range [-10, 10]
    
    # Evaluate the step function at the values of x
    y = step_function(x)
    
    # Approximate derivative of the step function
    y_deriv = np.zeros_like(x)  # The derivative is 0 over most of the domain (except at x=0, where there is a discontinuity)
    
    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the step function
    plt.plot(x, y, label='Step Function')  
    
    # Plot the approximate derivative (dashed green line)
    plt.plot(x, y_deriv, label='Approximate Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Title of the plot
    plt.title('Step Function and its Derivative')
    
    # Add a legend to identify the curves
    plt.legend()
    
    # Add grid to improve visibility
    plt.grid(True)
    
    # Display the plot on screen
    plt.show()

# Check if the script is executed directly
if __name__ == "__main__":
    plot_step_function()  # Call the function to plot the step function and its derivative
