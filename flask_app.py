# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('/home/indrami/mysite/model.pkl','rb'))
scaler = joblib.load(open('/home/indrami/mysite/scaler.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(scaler.transform([list(data.values())]))

    # Take the first value of prediction
    output = float(prediction[0])

    return jsonify(output)