import pandas as pd
import joblib
from fastapi import FastAPI , status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel , Field

#Model recall
with open("model/model_regression.joblib" , "rb") as r:
    model = joblib.load(r)

#Data recall
class data(BaseModel):
    Square_Feet:float = Field(... , gt = 0,description="House area in square feet",example=150.5)
    Num_Bedrooms:int = Field(... , ge = 1,le = 5,description="Number of bedrooms",example=3)
    Num_Bathrooms:int = Field(... , ge = 1,le = 3,description="Number of bathrooms",example=2)
    Num_Floors:int = Field(... , ge = 1,le = 3,description="Number of floors",example=2)
    Year_Built:int = Field(... , ge = 1900,le = 2022,description="Construction year",example=2015)
    Has_Garden:int = Field(... , ge = 0,le = 1,description="0 = No, 1 = Yes",example=1)
    Has_Pool:int = Field(... , ge = 0,le = 1,description="0 = No, 1 = Yes",example=0)
    Garage_Size:int = Field(... , ge = 10,le = 49,description="Garage capacity",example=20)
    Location_Score:float = Field(... , ge = 0,le = 10,description="Location quality score",example=8.5)
    Distance_to_Center:float = Field(... , ge = 0,le = 20,description="Distance to city center (km)",example=5.2)


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
    
    predict_data = pd.DataFrame({
        "Square_Feet": [input.Square_Feet],
        "Num_Bedrooms": [input.Num_Bedrooms],
        "Num_Bathrooms": [input.Num_Bathrooms],
        "Num_Floors": [input.Num_Floors],
        "Year_Built": [input.Year_Built],
        "Has_Garden": [input.Has_Garden],
        "Has_Pool": [input.Has_Pool],
        "Garage_Size": [input.Garage_Size],
        "Location_Score": [input.Location_Score],
        "Distance_to_Center": [input.Distance_to_Center]
})

    y_pred = float(model.predict(predict_data)[0])

    input_model = input.model_dump()
    dt.append(input_model)

    return {"prediction" : y_pred}

@app.get("/data" , status_code=status.HTTP_201_CREATED)
def get_data():
    return dt