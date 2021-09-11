from flask import Flask, render_template, request
from pathlib import Path
import os
from flask import jsonify
from werkzeug.utils import secure_filename
import warnings
warnings.filterwarnings("ignore")
from _bkcode.funct import *

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = Path('./_bkcode/uploads')

#"/" page
@app.route("/")
def hello_world():
    return "_Hello, World! from DIT"

#call when we want to predict just one observation (patient)
@app.route("/predict_one", methods = ["GET", "POST"])
def predict_one():
    page_ = "view_one.html"
    #dictionnary to send to the view.html
    dict_val_html = get_features_dict("-",6,148,72,35,0,33.6,0.627,50)
        
    if request.method == "GET":
        # if it is "GET", we load view.html with default parameters
        return render_template(page_, **dict_val_html)
    if request.method == "POST":
        #when submit form, we catch data from form
        pregnancy, glucose = request.form.get("pregnancy"), request.form.get("glucose")
        bloglucoseodpressure, skinthickness = request.form.get("bloglucoseodpressure"), request.form.get("skinthickness")
        insulin, bmi = request.form.get("insulin"), request.form.get("bmi")
        diabetespedigreefunction, age = request.form.get("diabetespedigreefunction"), request.form.get("age")
        
        #we put data in order in a list
        X = [pregnancy, glucose, bloglucoseodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]
        #prediction of patient X
        result = predict(X, load_model(), load_scaler())
        #we generate data and result to send to the view.html
        dict_val_html = get_features_dict(str(get_label(result, get_label_dict())[0])+" -- "+ str(result[0]) ,pregnancy,glucose,bloglucoseodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age) 
        #we call view.html
        return render_template(page_, **dict_val_html)


#call when we want to predict many observation (many patient) from CSV file
@app.route("/predict_many", methods = ["GET", "POST"])
def predict_many():
    
    page_ = "view_many.html"
    
    if request.method == "GET":
        return render_template(page_)
    if request.method == "POST":
        file = request.files['file']#recuperation du fichier uploadé
        filename = secure_filename(file.filename)#recuperation du nom du fichier uploadé
        full_path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)#Chemin complet vers notre fichier uploadé
        file.save(full_path_file)#Enregistrement dans le repertoire d'upload
        predictions = predict_(loaded_model=load_model(), scaler = load_scaler(), data = full_path_file) 
        return jsonify(str(predictions))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)