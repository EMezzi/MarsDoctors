from pydantic import BaseModel


class WaterData(BaseModel):
    # Returns negative
    ph: float = 0.7
    Hardness: float = 196
    Solids: float = 22014
    Chloramines: float = 7.12
    Sulfate: float = 333.78
    Conductivity: float = 426.21
    Organic_carbon: float = 14.28
    Trihalomethanes:float = 66.40
    Turbidity: float = 3.97

    # returns positive
    # {
    #     "ph": 9.79,
    #     "Hardness": 129.87,
    #     "Solids": 20682,
    #     "Chloramines": 9.39,
    #     "Sulfate": 291,
    #     "Conductivity": 427.12,
    #     "Organic_carbon": 11.85,
    #     "Trihalomethanes": 78.71,
    #     "Turbidity": 2.95
    # }

class GeneData(BaseModel):
    pass
