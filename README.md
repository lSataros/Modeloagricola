# Predicción Agrícola con Perceptrón Multicapa (MLP)

Este proyecto implementa un modelo de Perceptrón Multicapa (MLP) para realizar predicciones agrícolas utilizando datos históricos. El modelo ha sido desplegado localmente utilizando Flask, y el entorno de desarrollo recomendado es Visual Studio Code (VS Code).


##Drescripción

Este proyecto entrena un modelo de Perceptrón Multicapa para predecir la producción agrícola basada en datos históricos como año, área cultivada, rendimiento y producción nacional. El modelo se entrena y luego se despliega en un servidor Flask, permitiendo realizar predicciones mediante una API. Se presenta cómo aclaración en este punto que el modelo ofrece una predicción sobre el producto recomendable para cultivo en función del input en base a los datos provistos en cada versión del entrenamiento.

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

#Aquí dejamos cómo recurso la lista de comandos necesarios para operar: 
  -python -m venv venv
  
  -.\venv\Scripts\activate
  

Uso del Proyecto
1. Despliegue Local
Para desplegar el servidor Flask de forma local y hacer disponible el modelo para predicciones, ejecuta:  
  -python app.py
   
  Esto iniciará el servidor en http://127.0.0.1:5000/.

3. Realizar una Predicción
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
