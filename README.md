# Rainfall Prediction using Machine Learning Ensembles

## Overview

This project aims to predict rainfall within 1 hour and 24 hours at Soekarno-Hatta, Cengkareng International Airport, using machine learning ensembles. The predictions are based on observational surface atmospheric data collected from various weather stations in the region.

## Dataset

The dataset used for training and testing the models consists of historical weather data collected from multiple sources, including temperature, humidity, wind speed, atmospheric pressure, and other relevant features. The data is preprocessed and cleaned to handle missing values and ensure data consistency.

## Methodology

1. Data Preprocessing:
   - Handle missing values: Missing data is imputed using appropriate methods, such as mean, median, or interpolation.
   - Feature selection: Relevant features are selected based on their importance in predicting rainfall.
   - Data splitting: The dataset is divided into training and testing sets for model evaluation.

2. Feature Engineering:
   - Time-based features: Additional time-based features are extracted to capture temporal patterns.
   - Lagged variables: Lagged values of certain features are used to incorporate time dependencies.

3. Model Selection:
   - Ensemble Approach: We employ an ensemble of machine learning models to improve prediction accuracy and robustness.
   - Models considered include Random Forest, Gradient Boosting, and XGBoost.

4. Model Training:
   - Each model in the ensemble is trained on the training set using cross-validation to find optimal hyperparameters.
   - Model performance is evaluated based on metrics such as Mean Squared Error (MSE) and R-squared.

5. Prediction:
   - Once trained, the ensemble of models is used to make predictions on the testing set.

## Results

The models are evaluated based on their prediction performance, with a focus on accuracy and reliability in forecasting rainfall. The results will be presented through various visualization techniques to compare predicted rainfall with actual observed values.

## How to Use

To run the rainfall prediction models:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Prepare the observational surface atmospheric data and ensure it is in the correct format.
4. Run the prediction script with the provided data to generate rainfall predictions for 1 hour and 24 hours ahead.

## Conclusion

By utilizing machine learning ensembles and observational surface atmospheric data, this project aims to enhance the accuracy and efficiency of rainfall prediction at Soekarno-Hatta, Cengkareng International Airport. Accurate predictions can play a crucial role in mitigating the impact of extreme weather events and improving overall weather forecasting capabilities.

**Note**: The dataset used in this project may be subject to privacy and licensing constraints and is not publicly available. The code, however, serves as an example of how machine learning ensembles can be employed for rainfall prediction using similar datasets.
