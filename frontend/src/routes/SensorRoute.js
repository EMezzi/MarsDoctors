import React, {Component} from 'react';
import axios from "axios";
import {Button, Skeleton} from "antd";

import { Space, Table, Tag } from 'antd';
import {SearchOutlined, SendOutlined} from "@ant-design/icons";

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
        render: (text) => <Button type="primary"  icon={<SendOutlined />} onClick={() => {if (text === "normal") {console.log("Done")}}}>
            Send
        </Button>
    }
];
const data = [
    {
        key: '1',
        simulation: 'Good health and habitat data',
        action: 'normal'
    },
    {
        key: '2',
        simulation: 'Abnormal health and habitat',
        action: 'abnormal'
    },
];


class SensorRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
        }

        console.log("Loaded")

    }

    componentDidMount() {

        setTimeout(() => {
            this.setState({ loading: false });
        }, 500);

    }

    render() {

        return (
            <Table loading={this.state.loading} columns={columns} expandable={{
                expandedRowRender: (record) => (
                    <p
                        style={{
                            margin: 0,
                        }}
                    >
                        {record.explanation}
                    </p>
                ),
                rowExpandable: (record) => record.explanation !== 'Not Expandable',
            }} dataSource={data} />

        )

    }


}

export default SensorRoute;