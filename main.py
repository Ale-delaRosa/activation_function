import numpy as np  # Library for numerical operations with arrays
import matplotlib.pyplot as plt  # Library for creating plots

from src.gaussiana import plot_gaussian  # Function to plot a Gaussian distribution
from src.escalon import plot_step_function  # Function to plot the step function
from src.identidad import plot_identity  # Function to plot the identity function
from src.linear import plot_piecewise_func  # Function to plot a piecewise linear function
from src.relu import plot_relu  # Function to plot the ReLU function
from src.sigmoid import plot_sigmoid  # Function to plot the sigmoid function
from src.sinusoidal import plot_sinusoidal  # Function to plot a sinusoidal signal
from src.tanh import plot_tanh  # Function to plot the hyperbolic tangent

def main():
    print("Generado gráficas")  

    # Call each of the imported functions to generate the corresponding plots
    plot_gaussian()
    plot_step_function()
    plot_identity()
    plot_piecewise_func()
    plot_relu()
    plot_sigmoid()
    plot_sinusoidal()
    plot_tanh()

    print("Gráficas generadas correctamente.") 

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Calls the main function if the script is executed directly