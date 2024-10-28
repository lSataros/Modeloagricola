from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd


model = joblib.load('modelo_perceptron.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl') 

app = Flask(__name__)

@app.route('/')
def home():
  
    return render_template('index.html') 

# Definir la ruta para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del formulario
        year = request.form['year']
        area = request.form['area']
        rendimiento = request.form['rendimiento']
        produccion_nacional = request.form['produccion_nacional']
        
        # Validar que los datos no sean vacíos o contengan letras
        if not (year and area and rendimiento and produccion_nacional):
            return jsonify({'error': 'Todos los campos son requeridos y deben contener valores numéricos.'})

        # Convertir a flotante y validar que no sean cero ni valores inválidos
        try:
            year = float(year)
            area = float(area)
            rendimiento = float(rendimiento)
            produccion_nacional = float(produccion_nacional)
        except ValueError:
            return jsonify({'error': 'Los valores ingresados deben ser numéricos.'})

        # Verificar que los valores no sean cero
        if year <= 0 or area <= 0 or rendimiento <= 0 or produccion_nacional <= 0:
            return jsonify({'error': 'Los valores ingresados deben ser mayores que cero.'})

        # Crear un arreglo con los datos de entrada
        input_data = np.array([[year, area, rendimiento, produccion_nacional]])

        # Escalar los datos
        input_data_scaled = scaler.transform(input_data)

        # Realizar la predicción
        prediction = model.predict(input_data_scaled)

        # Decodificar la predicción para obtener el nombre del producto
        product = le.inverse_transform(prediction)[0]

        return jsonify({'prediction': f'Puedes cosechar: {product}'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
