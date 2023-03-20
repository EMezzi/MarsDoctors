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
    Trihalomethanes: float = 66.40
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
    # Returns positive
    s_at_11757650 = 5.376935
    s_at_11746506 = 8.215063
    a_at_11727942 = 6.360752
    a_at_11739534 = 5.635366
    x_at_11749460 = 5.273240
    x_at_11754604 = 7.672275
    x_at_11745837 = 5.308073
    x_at_11739536 = 5.810706
    x_at_11737944 = 7.846322
    x_at_11755730 = 7.782462
    a_at_11724463 = 4.551536
    a_at_11756809 = 6.141027
    a_at_11730501 = 6.357842


class HabitatData(BaseModel):
    ID: int = 6
    Setting: int = 2
    Post: int = 3
    SBP: int = 99
    DBP: int = 68
    STAI: int = 1.833
    PM2_5: int = 0
    Temp: int = 20.4
    Rh: int = 33.1
    CO2: int = 643
    Age: int = 27
    Sex: str = "Female"
    ethnic: str = "Asian"
    Healthcondition: str = "Very good"
    Medicine: str = "No"
    Sleep: str = "No"
    Caffinebeverage: str = "No"
    Stresslevel: int = 4
    Stress_or_not_after_test: str = "Yes"
    Which_part_first: int = 1
    Which_part_stress_most: int = 1
    VR_experience: str = "More than 3 times less than 10 times"
    Experience_Nature: int = 4
    Scence_1: int = 4
    Scence_2: int = 3
    Scence_3: int = 1
    Scence_4: int = 2


class SleepData(BaseModel):
    sr = 77.6
    rr = 21.76
    t = 93.76
    lm = 11.76
    bo = 91.76
    rem = 93.8
    sr = 4.64
    hr = 64.4
    sl = 2


class HeartData(BaseModel):
    # Returns positive
    age = 63
    sex = 1
    chest_pain_type = 3
    resting_bp = 145
    cholestoral = 233
    fasting_blood_sugar = 1
    restecg = 0
    max_hr = 150
    exang = 0
    oldpeak = 2.3
    slope = 0
    num_major_vessels = 0
    thal = 1
