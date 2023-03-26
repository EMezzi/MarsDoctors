import React from "react";
import {Card} from "antd";
import axios from "axios";
import {Bullet, Liquid} from '@ant-design/plots';

const data = [
    {
        title: 'Recoded ration levels',
        ranges: [10, 30, 100],
        measures: [7],
        target: 3,
    },
];

const config = {
    data:data,
    measureField: 'measures',
    height: 100,
    rangeField: 'ranges',
    targetField: 'target',
    xField: 'title',
    color: {
        range: ['#bfeec8', '#FFe0b0', '#FFbcb8'],
        measure: '#5B8FF9',
        target: '#39a3f4',
    },
    xAxis: {
        line: null,
    },
    yAxis: false,
    label: {
        target: true,
    },
    // 自定义 legend
    legend: {
        custom: true,
        position: 'bottom',
        items: [
            {
                value: 'Low',
                name: 'High Radiation',
                marker: {
                    symbol: 'square',
                    style: {
                        fill: '#FFbcb8',
                        r: 5,
                    },
                },
            },
            {
                value: 'Medium',
                name: 'Radiation detected',
                marker: {
                    symbol: 'square',
                    style: {
                        fill: '#FFe0b0',
                        r: 5,
                    },
                },
            },
            {
                value: 'High',
                name: 'Low radiation',
                marker: {
                    symbol: 'square',
                    style: {
                        fill: '#bfeec8',
                        r: 5,
                    },
                },
            },
            {
                value: 'Current',
                name: 'Current level',
                marker: {
                    symbol: 'square',
                    style: {
                        fill: '#5B8FF9',
                        r: 5,
                    },
                },
            },
            {
                value: 'Optimal',
                name: 'Maximum allowed level',
                marker: {
                    symbol: 'line',
                    style: {
                        stroke: '#39a3f4',
                        r: 5,
                    },
                },
            },
        ],
    },
};



class BulletCard extends React.Component {

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

    }

    render() {

        return(
            <Card  className='featuresCard' hoverable title="Radiation status" bordered={false} >

                <Bullet {...config}/>

            </Card>

        )

    }


}

export default BulletCard