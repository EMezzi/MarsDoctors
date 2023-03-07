from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
import pandas as pd

from models import WaterData
from machine_learning.waterPotabilityModel import WaterPotabilityModel

# Initialize app
app = FastAPI()

# TODO: Probably not gonna import everything in where and do prediction here.
waterModel = WaterPotabilityModel("latest")

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

    output = waterModel.predict(data)
    print(type(output))
    print(output.tolist())
    return {"input data": water_data, "output": output.tolist()[0]}