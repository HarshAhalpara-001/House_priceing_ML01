# House Price Predictor

Overview
House Price Predictor is a web application that predicts the selling price of a house based on its features and the selling prices of nearby houses. It utilizes machine learning algorithms to analyze real estate data and provide accurate price estimates.

Features
Input Form: Users can input various features of the house, such as location, number of bedrooms, bathrooms, living area, lot area, etc.<br>
Prediction Model: The application uses a multi-variable linear regression model trained on nearby houses' data to predict the selling price.<br>
Real-time Prediction: Predictions are made in real-time, allowing users to quickly assess the estimated price of a house.<br>
User-friendly Interface: The interface is intuitive and easy to use, providing users with a seamless experience.<br><br>
How It Works<br>
Input Data: Users input the features of the house they are interested in, including location, number of bedrooms, bathrooms, etc.<br>
Finding Nearest Houses: The application identifies the 15 closest houses to the given location using a k-nearest neighbors (kNN) algorithm.<br>
Training the Model: Based on the features of these nearest houses, a multi-variable linear regression model is trained to predict selling prices.<br>
Making Predictions: The model predicts the selling price of the input house based on its features.<br>
Displaying Predictions: The predicted price is displayed to the user, providing valuable insights for real estate decisions.<br>
Deployment<br>
The application can be deployed locally or on a web server using platforms like Heroku, AWS, or Google Cloud Platform.<br>

Installation<br>
To run the application locally, follow these steps:
<br>
Clone the repository: git clone https://github.com/your_username/house-price-predictor.git<br>
Run the backend server: python app.py<br>
Open index.html in a web browser to access the frontend.<br>
<br>Contributing<br>
Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.
