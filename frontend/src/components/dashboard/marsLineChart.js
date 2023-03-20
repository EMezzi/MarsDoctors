import React from "react";
import {Card, Skeleton} from "antd";
import { Line } from '@ant-design/plots';
import axios from "axios";
import PopoverHelp from "./popoverHelp";


let data = [
    {
        Date: "2034-01",
        scales: 89
    },
    {
        Date: "2034-02",
        scales: 92
    },
    {
        Date: "2034-03",
        scales: 87
    },
    {
        Date: "2034-04",
        scales: 120
    },
    {
        Date: "2034-05",
        scales: 86
    },
    {
        Date: "2034-06",
        scales: 84
    },
    {
        Date: "2034-07",
        scales: 60
    },
    {
        Date: "2034-08",
        scales: 84
    },
    {
        Date: "2034-09",
        scales: 90
    },
    {
        Date: "2034-10",
        scales: 99
    },
    {
        Date: "2034-11",
        scales: 96
    },
    {
        Date: "2034-12",
        scales: 95
    },
    {
        Date: "2034-13",
        scales: 94
    },
    {
        Date: "2034-14",
        scales: 87
    },
    {
        Date: "2034-15",
        scales: 84
    },
    {
        Date: "2034-16",
        scales: 79
    },
    {
        Date: "2034-17",
        scales: 85
    },
    {
        Date: "2034-18",
        scales: 86
    },
    {
        Date: "2034-19",
        scales: 114
    },
    {
        Date: "2034-20",
        scales: 92
    },
    {
        Date: "2034-21",
        scales: 88
    },
    {
        Date: "2034-22",
        scales: 89
    },
    {
        Date: "2034-23",
        scales: 84
    },
    {
        Date: "2034-24",
        scales: 76
    },
    {
        Date: "2034-25",
        scales: 81
    },
    {
        Date: "2034-26",
        scales: 81
    },
    {
        Date: "2034-27",
        scales: 85
    },
    {
        Date: "2034-28",
        scales: 78
    }
]

const probCardTitlePopup = "Hearth rate registry."

const probCardContentPopup = "Your hearth circulation system has been within limits in the past 30 days. No abnormal " +
    "values have been registered."

class MarsLineChart extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

    }


    componentDidMount() {

    }


    componentDidUpdate(prevProps, prevState, snapshot) {
        // This component shouldn't really change
    }

    render() {

        const config = {
            data,
            padding: 'auto',
            xField: 'Date',
            yField: 'scales',
            annotations: [
                {
                    type: 'regionFilter',
                    start: ['max', 'median'],
                    end: ['min', '120'],
                    color: '#F4664A',
                },
                {
                    type: 'text',
                    position: ['min', 'median'],
                    content: 'Warning',
                    offsetY: +15,
                    style: {
                        textBaseline: 'bottom',
                    },
                    color: '#F4664A',
                },
                {
                    type: 'line',
                    start: ['max', 'median'],
                    end: ['min', 'median'],
                    style: {
                        stroke: '#52d368',
                        lineDash: [2, 2],
                    },
                },
            ],
        };


        return(

            <Card  className='featuresCard' hoverable title="Heart Rate BPM (Month)" bordered={false} extra={<PopoverHelp title={probCardTitlePopup} content={probCardContentPopup}/>}>

                    <Line {...config} />

            </Card>

        )

    }


}

export default MarsLineChart