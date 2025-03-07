# Import necessary libraries
import numpy as np  # Library for mathematical operations and numerical array handling
import matplotlib.pyplot as plt  # Library for generating plots

# Definition of the function that plots the Gaussian function and its derivative
def plot_gaussian():
    ''' 
    Plots the Gaussian function (standard normal distribution) and its derivative.
    The Gaussian function is given by: f(x) = (1 / sqrt(2π)) * exp(-x² / 2).
    Its derivative is: f'(x) = -x * f(x).
    '''

    # Definition of the Gaussian function (standard normal distribution)
    def gaussian(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)  # Standard normal distribution formula

    # Derivative of the Gaussian function
    def gaussian_deriv(x):
        return -x * gaussian(x)  # Derivative of the Gaussian function with respect to x
    
    # Define the range of x values
    x = np.linspace(-10, 10, 400)  # Creates an array with 400 equally spaced values in the range [-10, 10]
    
    # Evaluate the Gaussian function at x values
    y = gaussian(x)
    
    # Evaluate the derivative of the Gaussian function at x values
    y_deriv = gaussian_deriv(x)
    
    # Create a figure for the plot
    plt.figure(figsize=(8, 6))  # Defines the figure size in inches (8x6)
    
    # Plot the Gaussian function
    plt.plot(x, y, label='Gaussian Function')  
    
    # Plot the derivative of the Gaussian function with a dashed green line
    plt.plot(x, y_deriv, label='Derivative', linestyle='--', color='green')
    
    # Axis labels
    plt.xlabel('x')
    plt.ylabel('Value')
    
    # Plot title
    plt.title('Gaussian Function and Its Derivative')
    
    # Add legend to identify the curves
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Check if the script is run directly
if __name__ == "__main__":
    plot_gaussian()  # Calls the function to plot the Gaussian function and its derivative