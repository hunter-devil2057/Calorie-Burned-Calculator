# **Calories Burned Calculator**

## Overview
The **Calories Burned Calculator** is a web application built using **Streamlit** and **Python** to estimate calories burned during a workout. It leverages a **Random Forest Regressor** model trained on a dataset of user attributes (gender, age, height, weight, workout duration, heart rate, and body temperature) to predict calorie expenditure with high accuracy (R² score: ~0.998). This project showcases the application of machine learning in fitness tracking, offering an intuitive interface for users to input data and receive instant predictions.

## Features
- **User-Friendly Interface**: Built with Streamlit for seamless input and output.
- **Accurate Predictions**: Uses a Random Forest Regressor trained on a dataset of 15,000 entries.
- **Input Parameters**: Gender, Age, Height, Weight, Workout Duration, Heart Rate, and Body Temperature.
- **Instant Results**: Displays predicted calories burned with a single click.

## Dataset
The model is trained on a dataset (`data.csv`) containing 15,000 records with the following features:
- **Gender**: Encoded as 0 (Male) or 1 (Female)
- **Age**: In years
- **Height**: In centimeters
- **Weight**: In kilograms
- **Duration**: Workout duration in minutes
- **Heart_Rate**: Average heart rate during workout
- **Body_Temp**: Body temperature in Celsius
- **Calories**: Target variable (calories burned)

The dataset is clean, with no missing values or duplicates, ensuring robust model performance.

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hunter-devil2057/Calorie-Burned-Calculator.git
   cd calories-burned-calculator
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Required packages: `streamlit`, `pandas`, `numpy`, `scikit-learn`, `pickle`.

3. **Download the Model**:
   Ensure the pre-trained model file (`model.pkl`) is in the project directory.

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   The app will open in your default web browser.

## Usage
1. Open the app in your browser.
2. Select your gender from the dropdown menu.
3. Enter your age, height (cm), weight (kg), workout duration (minutes), heart rate, and body temperature (Celsius).
4. Click the **Predict** button to view the estimated calories burned.

## Model Details
- **Algorithm**: Random Forest Regressor
- **Training**: Split into 80% training and 20% testing data
- **Performance**: Achieves an R² score of ~0.998 on the test set
- **Serialization**: The trained model is saved as `model.pkl` using `pickle`

## Project Structure
```
calories-burned-calculator/
├── app.py                 # Streamlit application
├── calorie-burned-calculator.ipynb  # Model training notebook
├── model.pkl              # Pre-trained Random Forest model
├── data.csv               # Dataset (not included in repo)
├── requirements.txt                # Project dependencies
├── README.md              # This file
```

## About Me
Hi, I'm **Manish Shiwakoti**, a passionate data analyst and developer with a focus on machine learning and web applications. Feel free to connect with me!

- **LinkedIn**: [Manish Shiwakoti](https://www.linkedin.com/in/manish-shiwakoti-01721b260/)
- **Instagram**: [manish.shiwakoti](https://www.instagram.com/manish.shiwakoti/)
- **Email**: [manishshiwakoti42@gmail.com](mailto:manishshiwakoti42@gmail.com)