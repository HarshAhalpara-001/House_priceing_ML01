from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import os

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://127.0.0.1:5500"}})  # Allow requests from your frontend origin

# Define the paths to the model and scaler files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')
KNN_MODEL_PATH = os.path.join(BASE_DIR, 'knn_model.pkl')
LINEAR_REGRESSION_MODEL_PATH = os.path.join(BASE_DIR, 'linear_regression_model.pkl')
DATASET_PATH = os.path.join(BASE_DIR, '..', 'data', 'House_Price_India.csv')  # Adjust the path to your dataset

# Load the saved models and scaler
with open(SCALER_PATH, 'rb') as file:
    scaler = pickle.load(file)

with open(KNN_MODEL_PATH, 'rb') as file:
    knn = pickle.load(file)

with open(LINEAR_REGRESSION_MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the request data
        data = request.json
        # Extract features for kNN
        query_point = pd.DataFrame({
            'Lattitude': [data['Lattitude']],
            'Longitude': [data['Longitude']]
        })

        # Scale the query point
        scaled_query_point = scaler.transform(query_point)

        # Find the k-nearest neighbors
        distances, indices = knn.kneighbors(scaled_query_point)

        # Retrieve the nearest rows
        nearest_rows = pd.read_csv(DATASET_PATH).iloc[indices[0]]

        # Define features for Linear Regression
        linear_features = [
            'number of bedrooms', 'number of bathrooms', 'living area', 'lot area', 
            'number of floors', 'waterfront present', 'number of views', 
            'condition of the house', 'grade of the house', 'Area of the house(excluding basement)', 
            'Area of the basement', 'Built Year', 'Renovation Year', 'Postal Code', 
            'living_area_renov', 'lot_area_renov', 
            'Number of schools nearby', 'Distance from the airport'
        ]

        # Prepare the training data
        X_train = nearest_rows[linear_features]
        y_train = nearest_rows['Price']

        # Define the point for prediction
        predict_point = pd.DataFrame({
            'number of bedrooms': [data['number_of_bedrooms']],
            'number of bathrooms': [data['number_of_bathrooms']],
            'living area': [data['living_area']],
            'lot area': [data['lot_area']],
            'number of floors': [data['number_of_floors']],
            'waterfront present': [data['waterfront_present']],
            'number of views': [data['number_of_views']],
            'condition of the house': [data['condition_of_the_house']],
            'grade of the house': [data['grade_of_the_house']],
            'Area of the house(excluding basement)': [data['area_of_the_house_excluding_basement']],
            'Area of the basement': [data['area_of_the_basement']],
            'Built Year': [data['built_year']],
            'Renovation Year': [data['renovation_year']],
            'Postal Code': [data['postal_code']],
            'living_area_renov': [data['living_area_renov']],
            'lot_area_renov': [data['lot_area_renov']],
            'Number of schools nearby': [data['number_of_schools_nearby']],
            'Distance from the airport': [data['distance_from_the_airport']]
        })

        # Make the prediction
        model.fit(X_train, y_train)
        prediction = model.predict(predict_point)
        return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
