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
    s_at_11757650 = 0,
    s_at_11746506 = 0,
    a_at_11727942 = 0,
    a_at_11739534 = 0,
    x_at_11749460 = 0,
    x_at_11754604 = 0,
    x_at_11745837 = 0,
    x_at_11739536 = 0,
    x_at_11737944 = 0,
    x_at_11755730 = 0,
    a_at_11724463 = 0,

    a_at_11756809 = 0,
    a_at_11730501 = 0,


class HabitatData(BaseModel):
    ID = 6,
    Setting = 2,
    Post = 3,
    SBP = 99,
    DBP = 68,
    STAI = 1.833,
    PM2_5 = 0,
    Temp = 20.4,
    Rh = 33.1,
    CO2 = 643,
    Age = 27,
    Sex = "Female",
    ethnic = "Asian",
    Healthcondition = "Very good",
    Medicine = "No",
    Sleep = "No",
    Caffinebeverage = "No",
    Stresslevel = 4,
    Stress_or_not_after_test = "Yes",
    Which_part_first = 1,
    Which_part_stress_most = 1,
    VR_experience = "More than 3 times less than 10 times",
    Experience_Nature = 4,
    Scence_1 = 4,
    Scence_2 = 3,
    Scence_3 = 1,
    Scence_4 = 2


class SleepData(BaseModel):
    sr = 77.6,
    rr = 21.76,
    t = 93.76,
    lm = 11.76,
    bo = 91.76,
    rem = 93.8,
    sr = 4.64,
    hr = 64.4,
    sl = 2


class HeartData(BaseModel):
    # Returns positive
    age = 63,
    sex = 1,
    chest_pain_type = 3,
    resting_bp = 145,
    cholestoral = 233,
    fasting_blood_suga = 1,
    restecg = 0,
    max_hr = 150,
    exang = 0,
    oldpeak = 2.3,
    slope = 0,
    num_major_vessels = 0,
    thal = 1
