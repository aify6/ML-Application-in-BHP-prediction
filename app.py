from distutils.command.install_egg_info import to_filename
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

def predictor(input_params):
    to_predict = np.array(input_params).reshape(1,8)
    model = pickle.load(open('DT.pkl','rb'))
    result = model.predict(to_predict)
    return result[0] 
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/", methods=["POST","GET"])
def results_pred():
    if request.method=="POST":
        to_predict = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = predictor(to_predict_list)
        prediction = str(result)
        print(prediction)
    return render_template("index.html",prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True)