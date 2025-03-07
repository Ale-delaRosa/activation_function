# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array manipulation
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the sinusoidal function and its derivative
def plot_sinusoidal():
    ''' 
    Plots the sinusoidal function (sine) and its derivative (cosine).
    The sine function is a fundamental trigonometric function used in signal processing and wave analysis.
    '''
  
    # Definition of the sinusoidal function
    def sin_func(x):
        return np.sin(x)  # Returns the sine of x
    
    # Derivative of the sinusoidal function
    def sin_deriv(x):
        return np.cos(x)  # The derivative of sine is cosine
    
    # Define the range of x values (from -2π to 2π)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # Generates 400 equally spaced values in the range [-2π, 2π]
    
    # Evaluate the sine function at x values
    y = sin_func(x)
    
    # Evaluate the derivative (cosine) at x values
    y_deriv = sin_deriv(x)

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the sinusoidal function
    plt.plot(x, y, label='Sinusoidal Function (sin x)')  
    
    # Plot the derivative of the sinusoidal function (cosine) with a dashed green line
    plt.plot(x, y_deriv, label='Derivative (cos x)', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Sinusoidal Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_sinusoidal()  # Calls the function to plot the sinusoidal function and its derivative