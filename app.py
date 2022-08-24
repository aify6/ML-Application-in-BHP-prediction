import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
 
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/", methods=["POST","GET"])
def results_pred():
    if request.method=="POST":
        result = request.form 
        for key,val in result.items():
            res= val
        # final_res = live_test(res)
    # return render_template("index.html",result=final_res)
if __name__ == "__main__":
    app.run(debug=True)
