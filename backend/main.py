from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
import pandas as pd

from models import WaterData, GeneData, SleepData, HabitatData, HeartData

from masterClass import MasterClass

# Initialize app
app = FastAPI()

# TODO: Probably not gonna import everything in where and do prediction here.

"""
Instantiate the Master object class. 
"""
masterObject = MasterClass()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MarsLife API",
        version="0.1",
        description="This API serves as an unified layer that helps collect data from Mars health and habitat sensors"
                    "and serves it to ML algorithms and heuristics to compute the well-being of astronauts on Mars.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def read_root():
    return {"message": "This is the API for MarsLife: An AI system that ensures a healthy and sustainable"
                       " lifestyle on Mars"}


@app.post("/predict_water_potability")
def predict_water_potability(water_data: WaterData):
    data = pd.DataFrame([water_data.dict()])
    print(data)

    output = masterObject.water_decide(data)
    print(type(output))
    print(output.tolist())
    return {"input data": water_data, "output": output.tolist()[0]}


@app.post("/predict_radiation_exposition")
def predict_radiation_exposition(genes_data: GeneData):
    data = pd.DataFrame([genes_data.dict()])
    output = masterObject.radiation_decide(data)

    return {'input data': genes_data, 'output': output}


@app.post("/predict_sleep_stress")
def predict_sleep_stress(sleep_data: SleepData):
    data = pd.DataFrame([sleep_data.dict()])
    output = masterObject.sleep_decide(data)

    return {'input data': sleep_data, 'output': output.tolist()[0]}


@app.post("/predict_habitat")
def predict_general_stress(habitat_data: HabitatData):
    data = pd.DataFrame([habitat_data.dict()])
    output = masterObject.habitat_decide(data)

    print("Questo è il risultato: ", output)

    return {'input data': habitat_data, 'output': output}


@app.post("/predict_heart_problems")
def predict_heart_stress(heart_data: HeartData):
    data = pd.DataFrame([heart_data.dict()])
    output = masterObject.heart_decide(data)

    return {'input data': heart_data, 'output': output}


@app.get("/notifications")
def predict_heart_stress():

    return masterObject.notifications
