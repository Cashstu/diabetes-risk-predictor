from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('xgb_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        gender = int(request.form['gender'])
        smoking = int(request.form['smoking_history'])

        features = [
            float(request.form['age']),
            int(request.form['hypertension']),
            int(request.form['heart_disease_history']),
            float(request.form['bmi']),
            float(request.form['hba1c_level']),
            float(request.form['blood_glucose']),
            # gender dummies
            1 if gender == 0 else 0,  # gender_female
            1 if gender == 1 else 0,  # gender_male
            1 if gender == 2 else 0,  # gender_other
            # smoking dummies
            1 if smoking == 0 else 0,  # smoking_history_current
            1 if smoking == 1 else 0,  # smoking_history_ever
            1 if smoking == 2 else 0,  # smoking_history_former
            1 if smoking == 3 else 0,  # smoking_history_never
            1 if smoking == 4 else 0,  # smoking_history_not current
            1 if smoking == 5 else 0,  # smoking_history_unknown
        ]

        input_data = np.array(features).reshape(1, -1)
        result = model.predict(input_data)
        prediction = 'Diabetes Detected' if result[0] == 1 else 'No Diabetes Detected'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)