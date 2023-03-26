import React from "react";
import {Card} from "antd";
import axios from "axios";
import {Bullet, Line, Liquid} from '@ant-design/plots';
import PopoverHelp from "./popoverHelp";
const config = {
    color: '#f62646',
    percent: 0.87,
    shape: function (x, y, width, height) {
        const r = width / 4;
        const dx = x - width / 2;
        const dy = y - height / 2;
        return [
            ['M', dx, dy + r * 2],
            ['A', r, r, 0, 0, 1, x, dy + r],
            ['A', r, r, 0, 0, 1, dx + width, dy + r * 2],
            ['L', x, dy + height],
            ['L', dx, dy + r * 2],
            ['Z'],
        ];
    },
    outline: {
        border: 4,
        distance: 8,
    },
    wave: {
        length: 128,
    },
};
class StressCard extends React.Component {


    constructor(props) {
        super(props);

    }


    componentDidMount() {

    }

    componentDidUpdate(prevProps, prevState, snapshot) {

    }

    render() {

        return(

            <Card  className='featuresCard' hoverable title="Overall status" bordered={false} >

                <Liquid {...config} />

            </Card>

        )

    }


}

export default StressCard