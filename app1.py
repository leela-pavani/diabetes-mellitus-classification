import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

from joblib import load
app = Flask(__name__)
model = pickle.load(open(r'C:\Users\DELL\Documents\Projects\CODE\CODE\decision2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    print(x_test)
    sc=load(r'C:\Users\DELL\Documents\Projects\CODE\CODE\scalar2.save')
    prediction = model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[0]
    if(output==0):
        return render_template('index.html', prediction_text='Patient have no chance of being diabetic'.format(output))
    else:
        return render_template('index.html', prediction_text='Patient have chance of being diabetic'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
