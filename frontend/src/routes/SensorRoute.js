import React, {Component} from 'react';
import axios from "axios";
import {Button, Table} from "antd";
import {SendOutlined} from "@ant-design/icons";

const waterData = {
    "ph": 0.7,
    "Hardness": 196,
    "Solids": 22014,
    "Chloramines": 7.12,
    "Sulfate": 333.78,
    "Conductivity": 426.21,
    "Organic_carbon": 14.28,
    "Trihalomethanes": 66.4,
    "Turbidity": 3.97
}

const radiationData = {
    "s_at_11757650": 5.376935,
    "s_at_11746506": 8.215063,
    "a_at_11727942": 6.360752,
    "a_at_11739534": 5.635366,
    "x_at_11749460": 5.27324,
    "x_at_11754604": 7.672275,
    "x_at_11745837": 5.308073,
    "x_at_11739536": 5.810706,
    "x_at_11737944": 7.846322,
    "x_at_11755730": 7.782462,
    "a_at_11724463": 4.551536,
    "a_at_11756809": 6.141027,
    "a_at_11730501": 6.357842
}

const sleepStressData = {
    "sr": 77.6,
    "rr": 21.76,
    "t": 93.76,
    "lm": 11.76,
    "bo": 91.76,
    "rem": 93.3,
    "sr1": 4.64,
    "hr": 64.4
}

const habitatStressData = {
    "ID": 6,
    "Setting": 2,
    "Post": 3,
    "SBP": 99,
    "DBP": 68,
    "STAI": 1.833,
    "PM2_5": 0,
    "Temp": 20.4,
    "Rh": 33.1,
    "CO2": 643,
    "Age": 27,
    "Sex": "Female",
    "Healthcondition": "Very good",
    "Medicine": "No",
    "Sleep": "No",
    "Caffinebeverage": "No",
    "Stresslevel": 4,
    "ethnic_Asian": 1,
    "ethnic_Black": 0,
    "ethnic_Latino": 0,
    "ethnic_Multiracial": 0,
    "ethnic_No": 0,
    "ethnic_Caucasian": 0,
    "Stress_or_not_after_test": "Yes",
    "Which_part_first": 1,
    "Which_part_stress_most": 1,
    "VR_experience": "More than 3 times less than 10 times",
    "Experience_Nature": 4,
    "Scence_1": 4,
    "Scence_2": 3,
    "Scence_3": 1,
    "Scence_4": 2
}

const heartData = {
    "age": 63,
    "sex": 1,
    "chest_pain_type": 3,
    "resting_bp": 145,
    "cholestoral": 233,
    "fasting_blood_sugar": 1,
    "restecg": 0,
    "max_hr": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "num_major_vessels": 0,
    "thal": 1
}


const data = [
    {
        key: '1',
        simulation: 'Health data checks',
        action: 'normal'
    },
    {
        key: '2',
        simulation: 'Habitat data checks',
        action: 'abnormal'
    },
];


class SensorRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            loading: false,
        }

        console.log("Loaded")
    }

    async sendHealthData() {

        let backEndUrl = 'http://127.0.0.1:8000/predict_radiation_exposition/'
        const radiationResponse = await axios.post(backEndUrl, radiationData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        backEndUrl = 'http://127.0.0.1:8000/predict_sleep_stress/'
        const sleepStressResponse = await axios.post(backEndUrl, sleepStressData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        backEndUrl = 'http://127.0.0.1:8000/predict_heart_problems/'
        const heartResponse = await axios.post(backEndUrl, heartData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        console.log(radiationResponse.data)
        console.log(sleepStressResponse.data)
        console.log(heartResponse.data)
    }

    async sendHabitatData() {

        let backEndUrl = 'http://127.0.0.1:8000/predict_water_potability/'
        const waterResponse = await axios.post(backEndUrl, waterData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        backEndUrl = 'http://127.0.0.1:8000/predict_habitat/'
        const habitatStressResponse = await axios.post(backEndUrl, habitatStressData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(waterResponse.data)
        console.log(habitatStressResponse.data)
    }

    componentDidMount() {

    }

    render() {

        const columns = [
            {
                title: 'Simulation',
                dataIndex: 'simulation',
                key: 'simulation',
            },
            {
                title: 'Action',
                key: 'action',
                dataIndex: 'action',
                render: (text) => <Button type="primary"  icon={<SendOutlined />} onClick={() =>
                {if (text === "normal") {this.sendHealthData()} else {this.sendHabitatData()}}}>
                    Send
                </Button>
            }
        ];
        return (
            <Table loading={this.state.loading} columns={columns} dataSource={data} />

        )

    }


}

export default SensorRoute;