import React from "react";
import {Card, Skeleton} from "antd";
import { Histogram } from '@ant-design/plots';
import axios from "axios";
import PopoverHelp from "./popoverHelp";

const config = {
    binField: 'value',
    binWidth: 0.1,
};


const probCardTitlePopup = "Density graph of expected probabilities on validation data"
const probCardContentPopup = "In the histogram below, we can see the distribution of the probabilities of a transaction " +
    "being fraudulent based on the validation historical dataset. This graph can help you get an idea of what a good " +
    "threshold would be when taking into account the total number of authorized/blocked transactions."

class DensityCard extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

        this.state = {
            loading:true,
            data: []
        }
    }

    loadData() {

        const backEndUrl = 'http://127.0.0.1:8000/prob_density'
        const getBackendData = async () => {
            try {
                const data = await axios.get(backEndUrl);
                this.setState({data: data.data})

            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading probabilities")
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

            <Card  className='featuresCard' hoverable title="Fraud probability distribution based on historical data" bordered={false} extra={<PopoverHelp title={probCardTitlePopup} content={probCardContentPopup}/>}>
                <Skeleton active={true} loading={this.state.loading}>
                    <Histogram data={this.state.data} {...config} />
                </Skeleton>
            </Card>

        )

    }


}

export default DensityCard