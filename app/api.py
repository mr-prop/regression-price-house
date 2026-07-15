import numpy as np
import joblib
from fastapi import FastAPI , status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

#Model recall
with open("model/model_regression.joblib" , "rb") as r:
    model = joblib.load(r)

#Data recall
class data(BaseModel):
    Square_Feet:Optional[float]
    Num_Bedrooms:Optional[int]
    Num_Bathrooms:Optional[int]
    Num_Floors:Optional[int]
    Year_Built:Optional[int]
    Has_Garden:Optional[int]
    Has_Pool:Optional[int]
    Garage_Size:Optional[int]
    Location_Score:Optional[float]
    Distance_to_Center:Optional[float]


dt = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.post("/predict" , status_code=status.HTTP_201_CREATED)
def prediction(input: data):
    
    predict_data_array = np.array([
        input.Square_Feet,
        input.Num_Bedrooms,
        input.Num_Bathrooms,
        input.Num_Floors,
        input.Year_Built,
        input.Has_Garden,
        input.Has_Pool,
        input.Garage_Size,
        input.Location_Score,
        input.Distance_to_Center
    ]).reshape(1 , -1)

    y_pred = float(model.predict(predict_data_array)[0])


    dt.append(input)

    return {"prediction" : y_pred}

@app.get("/data" , status_code=status.HTTP_201_CREATED)
def get_data():
    return dt