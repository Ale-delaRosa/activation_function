# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array handling
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots a piecewise function and its derivative
def plot_piecewise_func():
    ''' 
    Plots a piecewise function and its derivative.
    The function has three segments: a constant, a linear, and another constant part.
    '''
    
    # Definition of the piecewise function
    def piecewise_func(x):
        return np.piecewise(x, 
                            [x < -1, (x >= -1) & (x <= 1), x > 1],  # Conditions for each segment
                            [lambda x: -1, lambda x: x, lambda x: 1])  # Corresponding values for each segment

    # Derivative of the piecewise function
    def piecewise_func_deriv(x):
        return np.piecewise(x, 
                            [x < -1, (x > -1) & (x < 1), x > 1],  # Define intervals where the derivative changes
                            [0, 1, 0])  # The derivative is 0 outside (-1,1) and 1 inside the open interval (-1,1)

    # Define the range of x values
    x = np.linspace(-3, 3, 500)  # Creates an array with 500 equally spaced values in the range [-3, 3]
    
    # Evaluate the piecewise function at x values
    y = piecewise_func(x)
    
    # Evaluate the derivative of the piecewise function at x values
    y_deriv = piecewise_func_deriv(x)

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the piecewise function
    plt.plot(x, y, label='Piecewise Function')  
    
    # Plot the derivative of the piecewise function with a dashed green line
    plt.plot(x, y_deriv, label='Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Piecewise Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_piecewise_func()  # Calls the function to plot the piecewise function and its derivative