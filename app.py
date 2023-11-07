from flask import Flask, render_template, request
import numpy as np
import pickle
#import joblib
app = Flask(__name__)
filename = 'breast_cancer.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    try:
        Uniformity_cell_shape = int(request.form['uniformity_cell_shape'])
        Bare_nuclei = int(request.form['bare_nuclei'])
        Bland_chromatin = int(request.form['bland_chromatin'])
        Normal_nucleoli = int(request.form['normal_nucleoli'])

        if (1 <= Uniformity_cell_shape <= 10) and (1 <= Bare_nuclei <= 10) and (1 <= Bland_chromatin <= 10) and (1 <= Normal_nucleoli <= 10):
            pred = model.predict(np.array([[Uniformity_cell_shape, Bare_nuclei, Bland_chromatin, Normal_nucleoli]]))
            return render_template('index.html', predict=str(pred))
        else:
            return render_template('index.html', predict='Please enter values between 1 and 10.')
    except ValueError:
        return render_template('index.html', predict='Please enter integer values between 1 and 10.')
        pred = model.predict(np.array([[Uniformity_cell_shape, Bare_nuclei, Bland_chromatin, Normal_nucleoli ]]))
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    app.run(debug=True)
