from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved models
ridge_model = joblib.load('Models/ridge_model.pkl')
logistic_model = joblib.load('Models/logistic_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependents = int(request.form['dependents'])
    education = int(request.form['education'])
    self_employed = int(request.form['self_employed'])
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = float(request.form['credit_history'])
    property_area = int(request.form['property_area'])

    # transformation using log transformer
    applicant_income_log = np.log1p(applicant_income)
    coapplicant_income_log = np.log1p(coapplicant_income)
    loan_amount_log = np.log1p(loan_amount)
    loan_amount_term_log = np.log1p(loan_amount_term)

    # Prepare the input data as a list
    input_data = [[gender, married, dependents, education, self_employed, credit_history, property_area, 
                   applicant_income_log, coapplicant_income_log,
                   loan_amount_log, loan_amount_term_log]]
    

    # Use the models to make predictions
    ridge_prediction = ridge_model.predict(input_data)
    logistic_prediction = logistic_model.predict(input_data)

    # setting classification threshold
    threshold = 0.5

    # Map the prediction values to the respective labels
    ridge_result = 'Approved' if ridge_prediction[0] >= threshold else 'Not Approved'
    logistic_result = 'Approved' if logistic_prediction[0] >= threshold else 'Not Approved'

    return render_template('index.html', ridge_result=ridge_result, logistic_result=logistic_result)

if __name__ == '__main__':
    app.run(debug=True)

