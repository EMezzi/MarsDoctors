import React, {Component} from 'react';
import axios from "axios";
import {Button} from "antd";

import { Space, Table, Tag } from 'antd';
import {SyncOutlined} from "@ant-design/icons";

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

class HistoryRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            data: []
        }

        console.log("Loaded")

    }

    /**
     * Get notifications
     */
    async getNotifications() {

        const backEndUrl_threshold = 'http://127.0.0.1:8000/notifications/'
        const getBackendData = async () => {
            try {
                const data_notifications = await axios.get(backEndUrl_threshold);
                this.setState({data: data_notifications.data})
            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading notifications")
                this.setState({loading: false})
            }
        };

        getBackendData()
    }

    componentDidMount() {

        // setTimeout(() => {
        //     this.setState({ loading: false });
        // }, 500);
        this.getNotifications()

    }

    render() {

        return (
            <div>
                <Button className="refreshButton" shape="round" type="primary" icon={<SyncOutlined />} onClick={async () => {
                    this.setState({loading: true});
                    await new Promise(r => setTimeout(r, 200));
                    this.getNotifications()
                }}>

                </Button>
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
                }} dataSource={this.state.data} />
            </div>


        )

    }


}

export default HistoryRoute;