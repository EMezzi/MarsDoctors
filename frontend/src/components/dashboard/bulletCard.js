import React from "react";
import {Card} from "antd";
import axios from "axios";
import { Bullet } from '@ant-design/plots';



const config = {
    measureField: 'measures',
    height: 100,
    rangeField: 'ranges',
    targetField: 'target',
    xField: 'title',
    color: {
        range: ['#FFbcb8', '#FFe0b0', '#bfeec8'],
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
                name: 'Low recall',
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
                name: 'Medium recall',
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
                name: 'High recall',
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
                name: 'Current recall',
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
                name: 'Optimal recall',
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

        this.state = {
            loading: true,
        }
        this.data = [
            {
                title: 'Blocked fraud',
                ranges: [30, 70, 100],
                measures: [parseInt(this.props.true_recall.recall * 100)],
                target: 100,
            },
        ];

    }


    componentDidMount() {
        //this.loadData()
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (prevProps.true_recall !== this.props.true_recall) {
            console.log("updated")
            this.data = [
                {
                    title: 'Blocked fraud',
                    ranges: [30, 70, 100],
                    measures: [parseInt(this.props.true_recall.recall * 100)],
                    target: 100,
                },
            ];
            this.render()
        }
    }

    render() {

        return(

            // <Bullet {this.data, ...config} />
            <Bullet data={this.data} {...config}/>
        )

    }


}

export default BulletCard