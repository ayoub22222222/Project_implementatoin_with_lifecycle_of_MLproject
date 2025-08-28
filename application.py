from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

applictaion = Flask(__name__)
app = applictaion


ridge_model = pickle.load(open("ridge.pkl", "rb"))
standard_scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        RH = float(request.form["RH"])
        Ws = float(request.form["Ws"])
        Rain = float(request.form["Rain"])
        FFMC = float(request.form["FFMC"])
        DMC = float(request.form["DMC"])
        ISI = float(request.form["ISI"])
        Classes = int(request.form["Classes"])
        Region = int(request.form["Region"])

        scaler = standard_scaler.transform([[temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(scaler)
        return render_template("home.html", results = result[0])
    else:
        return render_template("home.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0")
