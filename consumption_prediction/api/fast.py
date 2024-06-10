from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Unpickle saved model
app.state.model = pickle.load(open('xgb_model.pkl', 'rb'))


# Define a root `/` endpoint
@app.get('/')
def index():
 return {'ok': True}


# Define a `/predict` endpoint
@app.post('/predict')
def predict(dynamic_features: dict):

    hidden_features = {
        'temp_mean': 8.846784796250905,
        'temp_min': 5.772831652443755,
        'temp_max': 12.269387121799843,
        'entry_floor': 0.6943588606893495,
        'income_band_num': 6.117300232738557,
        'electric_appliance': 7.8318962651002995,
        'gas_appliance': 3.623473345893827,
        'total_area': 859.6971073922199,
        'windowsopen': 5.805297572869334,
        'mean_h': 51.72884702264284,
        'min_h': 47.39651056424444,
        'max_h': 57.8116507886928,
        'average_age_numeric': 38.89990210203554,
        'total_participants': 2.436528870663859}

    # Define other_features for testing purposes
    other_features = {
        'residents': 2.43830211681259,
        'room_count': 8.602748531530533,
        'workstatus': 0.14854298274779265,
        'hometype': 'house_or_bungalow'
    }

    #combine static and dynamic features into a single dict
    features = {**hidden_features, **dynamic_features}

    # Prediction Value
    prediction = app.state.model.predict(pd.DataFrame(features, index=[0]))
    return {'prediction': prediction[0].tolist()}
