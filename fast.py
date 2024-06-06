from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import numpy as np
import joblib
import streamlit


app = FastAPI()

# Define a Pydantic model for the request body
class PredictionRequest(BaseModel):
    datetime: str
    homeid: int
    gas_kWh: float
    total_kWh: float
    temp_mean: float
    temp_min: float
    temp_max: float
    location_id: int
    location_name: str
    gas_appliance: int
    total_area: float
    room_count: int
    windowsopen: int
    mean_h: float
    min_h: float
    max_h: float
    mean_t: float
    min_t: float
    max_t: float
    residents: int

# Define a Pydantic model for the response body
class PredictionResponse(BaseModel):
    datetime: str
    location_name: str
    homeid: int
    room_count: int
    total_area: float
    temp_mean: float
    total_kWh: float
    residents: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the consumption prediction API"}

@app.post("/predict", response_model=PredictionResponse)
def predict_consumption(request: PredictionRequest):
    # Extract data from request
    data = {
        'datetime': request.datetime,
        'homeid': request.homeid,
        'gas (kWh)': request.gas_kWh,
        'Total (kWh)': request.total_kWh,
        'temp_mean': request.temp_mean,
        'temp_min': request.temp_min,
        'temp_max': request.temp_max,
        'location_id': request.location_id,
        'location_name': request.location_name,
        'gas_appliance': request.gas_appliance,
        'total_area': request.total_area,
        'room_count': request.room_count,
        'windowsopen': request.windowsopen,
        'mean_h': request.mean_h,
        'min_h': request.min_h,
        'max_h': request.max_h,
        'mean_t': request.mean_t,
        'min_t': request.min_t,
        'max_t': request.max_t,
        'residents': request.residents,
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Preprocess data (this part should match your preprocessing steps during training)
    df = preprocess_data(df)

    # Load the trained model
    model = load_model()

    # Make predictions
    df['predicted_total_kWh'] = model.predict(df)

    # Prepare the response
    response = {
        "Location": request.location_name,
        "Number of rooms": request.room_count,
        "Number if people": request.residents
        "total_kWh": df['predicted_total_kWh'].iloc[0]
    }

    return PredictionResponse(**response)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # Placeholder for preprocessing steps
    # Implement your actual preprocessing logic here
    return df

def load_model():
    # Placeholder for loading the model
    # Replace this with code to load your trained model, e.g., using joblib
    model = joblib.load("path_to_your_trained_model.pkl")
    return model

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
