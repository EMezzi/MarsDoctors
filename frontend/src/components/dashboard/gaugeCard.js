import React from "react";
import {Card} from "antd";
import axios from "axios";

import { Gauge } from '@ant-design/plots';
import PopoverHelp from "./popoverHelp";

const estimatedCardTitlePopup = "How many fraudalent transaction are estimated to be blocked"
const estimatedCardContentPopup = "In this card you can see an estimated percentage of blocked transactions based " +
    "on the threshold set above. This number is computed based on a validation dataset and only serves as an indication " +
    "to how the model will perform on new data."

class GaugeCard extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

        this.config = {
            percent: (this.props.true_recall.recall).toFixed(2),
            range: {
                color: 'l(0) 0:#FF0000 1:#00FF00',
            },
            startAngle: Math.PI,
            endAngle: 2 * Math.PI,
            indicator: null,
            statistic: {
                title: {
                    offsetY: -70,
                    style: {
                        fontSize: '50px',
                        color: '#4B535E',
                    },
                    formatter: () => parseInt(this.config.percent * 100) + "%",
                },
                content: {
                    style: {
                        fontSize: '24px',
                        lineHeight: '20px',
                        color: '#4B535E',
                    },
                    formatter: () => 'Fraud blocked',
                },
            },
        };
    }

    componentDidMount() {

    }


    componentDidUpdate(prevProps, prevState, snapshot) {
        this.config.percent = (this.props.true_recall.recall).toFixed(2)
    }

    render() {

        return(
            <Card  className='featuresCard' hoverable title="Estimated fraud transactions blocked" bordered={false} extra={<PopoverHelp title={estimatedCardTitlePopup} content={estimatedCardContentPopup}/>}>
                <Gauge {...this.config} />
            </Card>
        )

    }


}

export default GaugeCard