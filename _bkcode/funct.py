import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

#load model and return
def load_model(path_model = "_bkcode/model/model_rf.hd5"):
    return pickle.load(open(path_model, 'rb'))

#load scaler and return
def load_scaler(path_scaler = "_bkcode/model/scaler_standard.pkl"):
    return pickle.load(open(path_scaler, 'rb'))

# get the label dictionnary
def get_label_dict():
    return {
        1:"Diabétique",
        0: "Pas diabétique"
        }
    
# get the label corresponding to a prediction
def get_label(y_pred, dict_label):   
    return [dict_label.get(int(y)) for y in y_pred]

#prediction function
def predict(X, model, scaler):
    """
    X : the set of values to predict. We assume that X is not standardize
    X format: [Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin, BMI,	DiabetesPedigreeFunction, Age]
    return the value of prediction
    """    
    _X = (np.array(X).reshape(1, -1) if isinstance(X, list) else X)
    X_s = scaler.transform(_X)
    return model.predict(X_s)

def predict_(loaded_model, scaler, data= 'diabetes.csv'): 
    #data
    diabete_db = pd.read_csv(data)

    #standarisation of the series
    X=diabete_db.drop("Outcome",axis=1).values
    X_s=scaler.transform(X) 
          
    y_preds = loaded_model.predict(X_s)

    return y_preds


#get features in dictionary
def get_features_dict(*args):
    return {"resultat": args[0],
            "pregnancy": args[1],
            "glucose": args[2],
            "bloglucoseodpressure": args[3],
            "skinthickness": args[4],
            "insulin": args[5],
            "bmi": args[6],
            "diabetespedigreefunction": args[7],
            "age": args[8]
            }



