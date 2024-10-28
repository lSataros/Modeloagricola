# Predicción Agrícola con Perceptrón Multicapa (MLP)

Este proyecto implementa un modelo de Perceptrón Multicapa (MLP) para realizar predicciones agrícolas utilizando datos históricos. El modelo ha sido desplegado localmente utilizando Flask, y el entorno de desarrollo recomendado es Visual Studio Code (VS Code).


##Drescripción

Este proyecto entrena un modelo de Perceptrón Multicapa para predecir la producción agrícola basada en datos históricos como año, área cultivada, rendimiento y producción nacional. El modelo se entrena y luego se despliega en un servidor Flask, permitiendo realizar predicciones mediante una API. Se presenta cómo aclaración en este punto que el modelo ofrece una predicción sobre el producto recomendable para cultivo en función del input en base a los datos provistos en cada versión del entrenamiento.


app.py:  Contiene la lógica principal del modelo.

modelo_perceptron.pkl:  Contiene el modelo entrenado.

scaler.pkl:  Utiliza un StandardScaler para asegurar que la proporción de los datos coincida con la que el modelo espera obtener.

label_encoder.pkl:  Ayudará a desplegar el nombre del producto en base a su corresponidente valor número en la operación.



##Requisitos previos

Antes de comenzar, asegúrate de tener los siguientes componentes instalados:
- Python 3.8 o superior.
- Visual Studio Code (VS Code).
- `pip` para la instalación de paquetes:

-numpy

-matplotlib

-de flask: Flask, request, jsonify, render_template

-pandas

-scikit-learn

-joblib

   
- Conexión a internet para la descarga de paquetes y dependencias.



#Aquí dejamos cómo recurso la lista de comandos necesarios para generar un entorno vitual si es lo deseable: 
  
  -python -m venv venv
  
  -.\venv\Scripts\activate
  

Uso del Proyecto_

1. Despliegue Local
Para desplegar el servidor Flask de forma local y hacer disponible el modelo para predicciones, ejecuta:  
  -python app.py
   
  Esto iniciará el servidor en http://127.0.0.1:5000/.

2. Realizar una Predicción
   
Puedes hacer una predicción enviando una solicitud POST a la API:

URL: http://127.0.0.1:5000/predict

Método: POST

Aclaración: el formato de entrada será JSON y a continuación un ejemplo de los datos que se pueden proporcionar: 

    {
    "Año": 2023,
    "Area (ha)": 1500,
    "Rendimiento (ha/ton)": 3.5,
    "Produccion Nacional (ton)": 5000
}  




Colaboradores:

Este proyecto fue desarrollado por un equipo de estudiantes del bootcamp de inteligencia artificial y talento tech, versión 2, de MINTIC.

Campistas:

Laura Sofía Luna Duque

Edilberto Salazar García

Christian Javier Uchima Sierra

Adriana María Vélez

Ismael Vasco

Gustavo Rodriguez
