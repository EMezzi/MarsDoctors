import React, {Component} from 'react';
import axios from "axios";
import {Skeleton} from "antd";

import { Space, Table, Tag } from 'antd';

const columns = [
    {
        title: 'Name',
        dataIndex: 'name',
        key: 'name',
    },
    {
        title: 'Date',
        dataIndex: 'date',
        key: 'date',
    },
    {
        title: 'Description',
        dataIndex: 'description',
        key: 'description',
    },
    {
        title: 'Tags',
        key: 'tags',
        dataIndex: 'tags',
        render: (_, { tags }) => (
            <>
                {tags.map((tag) => {
                    let color = "green"
                    if (tag === 'warning') {
                        color = 'yellow';
                    }
                    if (tag === 'bad') {
                        color = 'red';
                    }
                    return (
                        <Tag color={color} key={tag}>
                            {tag.toUpperCase()}
                        </Tag>
                    );
                })}
            </>
        ),
    },
    {
        title: 'Action',
        key: 'action',
        render: (_, record) => (
            <Space size="middle">
                <a>Delete</a>
            </Space>
        ),
    },
];
const data = [
    {
        key: '1',
        name: 'Health check',
        date: "10-01-2045",
        description: 'No action needed.',
        explanation: 'Longer explanation Longer explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanationLonger explanation',
        tags: ['good'],
    },
    {
        key: '2',
        name: 'Habitat check',
        date: "11-01-2045",
        description: 'No action needed.',
        explanation: 'Longer explanation',
        tags: ['good'],
    },
    {
        key: '3',
        name: 'Health check',
        date: "12-01-2045",
        description: 'Detected increasing stress level!',
        explanation: 'Longer explanation',
        tags: ['warning'],
    },
];


class HistoryRoute extends Component {

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

export default HistoryRoute;