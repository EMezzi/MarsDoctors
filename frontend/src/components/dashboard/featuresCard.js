import React from "react";
import {Card} from "antd";
import { Bar } from '@ant-design/plots';
import axios from "axios";
import PopoverHelp from "./popoverHelp";


const config = {
    xField: 'importance',
    yField: 'feature',
    seriesField: 'feature',
    legend: {
        position: 'top-left',
    },
};

const explainabilityCardTitlePopup = "Variables used in the ML model"
const explainabilityCardContentPopup = "This card contains an interactive plot of all the variables used by our model when " +
    "predicting whether a new transaction is fraudulent or not. These cannot be changed, but on the x-axis, their importance " +
    "is displayed. No user-sensitive data is used when predicting an outcome."


/**
 *
 */
class FeaturesCard extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            model_features: []
        }
    }

    loadData() {

        const backEndUrl = 'http://127.0.0.1:8000/feature_importance/'
        const getBackendData = async () => {
            try {
                const data = await axios.get(backEndUrl);
                this.setState({model_features: data.data})
                console.log(data.data)

            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading features")
                this.setState({loading: false})
            }
        };

        getBackendData()
    }


    componentDidMount() {
        this.loadData()
    }


    componentDidUpdate(prevProps, prevState, snapshot) {
        // This component shouldn't really change
    }

    render() {

        return(
            <Card  className='featuresCard' hoverable title="Global model explainability" bordered={false} extra={<PopoverHelp title={explainabilityCardTitlePopup} content={explainabilityCardContentPopup}/>}>
                <Bar data={this.state.model_features} {...config} />
            </Card>
        )

    }


}

export default FeaturesCard