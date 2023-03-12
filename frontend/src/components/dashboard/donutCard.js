import React from "react";
import {Card} from "antd";
import axios from "axios";
import { Pie } from '@ant-design/plots';


const data = [
    {
        type: 'Blocked',
        value: 92,
    },
    {
        type: 'Allowed',
        value: 8,
    }
];
const config = {
    appendPadding: 10,
    data,
    angleField: 'value',
    colorField: 'type',
    radius: 1,
    innerRadius: 0.6,
    label: {
        type: 'inner',
        offset: '-50%',
        content: '{value}',
        style: {
            textAlign: 'center',
            fontSize: 14,
        },
    },
    interactions: [
        {
            type: 'element-selected',
        },
        {
            type: 'element-active',
        },
    ],
    statistic: {
        title: false,
        content: {
            style: {
                whiteSpace: 'pre-wrap',
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                fontSize: 15
            },
            content: 'Blocked\nTransactions',
        },
    },
};

class DonutCard extends React.Component {

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
            <Card  className='featuresCard' hoverable title="Fraud transactions" bordered={false}>
                <Pie {...config} />
            </Card>
        )

    }


}

export default DonutCard