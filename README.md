Funciones de Activación para Redes Neuronales 🔥
👤 Autor: Alejandro Garcia
📅 Fecha: 7 de marzo
📷 Instagram: @ale_garcia454

🚀 Este proyecto implementa y analiza diferentes funciones de activación utilizadas en redes neuronales para clasificación de dígitos manuscritos. Las funciones de activación juegan un papel crucial en la capacidad de la red para aprender y realizar predicciones.

Funciones de Activación Utilizadas
1. ReLU (Rectified Linear Unit)
La función ReLU es ampliamente utilizada en redes neuronales profundas debido a su simplicidad y eficiencia computacional. Permite que la red sea no lineal, mientras evita el problema del desvanecimiento del gradiente.
2. Sigmoidal
La función sigmoidal mapea cualquier valor de entrada al rango entre 0 y 1, lo que la hace útil en tareas de clasificación binaria, aunque puede sufrir del problema del desvanecimiento del gradiente.
3. Escalón (Heaviside)
La función escalón es una de las más simples. No es diferenciable en x=0, pero es útil en ciertas aplicaciones de clasificación. Sin embargo, rara vez se usa hoy en día debido a su falta de suavidad.
4. Gaussiana
La función gaussiana o "campana de Gauss" es útil cuando se requiere una activación que decaiga rápidamente desde el centro hacia los extremos. Se usa en redes neuronales de tipo RBF (Radial Basis Function).
5. Identidad
La función de identidad no cambia la entrada, lo que significa que simplemente pasa los valores tal cual como son. Se usa generalmente en la capa de salida de redes neuronales para regresión.
6. Linear
Similar a la función de identidad, pero con un factor de escala a y un sesgo b. Se utiliza cuando la salida de la red neuronal necesita ser una combinación lineal de las entradas.
7. Sinusoidal
Esta función introduce una forma de onda sinusoidal en las activaciones. Puede ser útil en tareas donde se requiere modelar relaciones periódicas, aunque no es muy común en redes neuronales estándar.
8. Tanh (Tangente Hiperbólica)
La función tanh es similar a la sigmoidal, pero su salida está en el rango de -1 a 1. Ayuda a centrar los datos alrededor de cero, lo que puede facilitar el entrenamiento de la red.
🎯 Características
👉 Implementación de múltiples funciones de activación.
👉 Análisis de su impacto en el rendimiento de una red neuronal.
👉 Comparación entre funciones lineales y no lineales.
👉 Aplicación práctica en clasificación de dígitos manuscritos utilizando el conjunto de datos MNIST.

🔧 Requisitos
Asegúrate de tener instaladas las siguientes librerías antes de ejecutar el código:

bash
Copiar
Editar
pip install numpy keras tensorflow matplotlib
🚀 Uso
Para ejecutar el código, simplemente corre el siguiente comando en tu terminal:

bash
Copiar
Editar
python main.py
Esto entrenará la red neuronal con el dataset MNIST y aplicará las funciones de activación mencionadas.

📚 Estructura del Proyecto
La estructura del proyecto es la siguiente:

📂 main/
👉📂 src/
👉 📂 pycache/
👉 📄 neural_network_keras.py
👉📄 .gitignore
👉📄 README.md
👉📄 requirements.txt

Autor
📌 Desarrollado por Alejandro Garcia.
