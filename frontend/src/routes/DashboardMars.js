import React, {Component, useState} from 'react';
import axios from "axios";
import "../css/App.css"
import {Button, Card, Col, InputNumber, Row, Skeleton, Slider,notification} from "antd";
import {Content} from "antd/es/layout/layout";
import {CloudFilled, DashboardOutlined, DislikeOutlined, LikeOutlined} from "@ant-design/icons";

import { SmileOutlined } from '@ant-design/icons';
import MarsLineChart from "../components/dashboard/marsLineChart";


class DashboardMars extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);



    }

    componentDidMount() {
        // function to show the notification
        const showNotification = () => {
            notification.info({
                message: 'Health Check Complete',
                description:
                    'Your health check has been completed successfully. No abnormal conditions have been identified.',
                duration: 0,
            });
        };

        const showNotification2 = () => {
            notification.warning({
                message: 'Habitat Check Complete',
                description:
                    'Your habitat check has been completed successfully. Abnormal behavior has been reported. Please ' +
                    'check notification tabs!',
                duration: 0,
                // className: 'custom-class',
                // style: {
                //     width: 600,
                // },
            });
        };

// call the showNotification function after 10 seconds
        setTimeout(showNotification, 2000); // 2000 milliseconds = 2 seconds
        setTimeout(showNotification2, 6000); // 3000 milliseconds = 3 seconds
    }


    componentDidUpdate(prevProps, prevState, snapshot) {

    }

    render() {


        return (
            <Content>

                <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                    <Col className="topCards" flex="auto">
                        <Card bodyStyle={{
                            height: '9vh'
                        }} className='transactionTest' hoverable bordered={false}>
                            <div className="alignment">
                                <div className="mainText">
                                    <div className="smallCardTitle">
                                    <span>
                                        Last check
                                    </span>
                                    </div>

                                    <div className="smallCardContent">
                                    <span>
                                        Today
                                    </span>
                                    </div>
                                </div>

                            </div>
                            <DashboardOutlined className="smallCardIcon"/>

                        </Card>
                    </Col>
                    <Col className="topCards" flex="auto">
                        <Card bodyStyle={{
                            height: '9vh'
                        }} className='transactionTest' hoverable bordered={false}>

                            <div className="alignment">
                                <div className="mainText">
                                    <div className="smallCardTitle">
                                    <span>
                                        Current health status
                                    </span>
                                    </div>

                                    <div className="smallCardContent">
                                    <span>
                                        Good
                                    </span>
                                    </div>
                                </div>

                            </div>
                            <LikeOutlined className="smallCardIcon"/>
                        </Card>
                    </Col>
                    <Col className="topCards" flex="auto">
                        <Card bodyStyle={{
                            height: '9vh'
                        }} className='transactionTest' hoverable bordered={false}>

                            <div className="alignment">
                                <div className="mainText">
                                    <div className="smallCardTitle">
                                    <span>
                                        Current habitat status
                                    </span>
                                    </div>

                                    <div className="smallCardContent">
                                    <span>
                                        Moderate
                                    </span>
                                    </div>
                                </div>

                            </div>
                            <DislikeOutlined className="smallCardIcon"/>
                        </Card>
                    </Col>
                    <Col className="topCards" flex="auto">
                        <Card bodyStyle={{
                            height: '9vh'
                        }} className='transactionTest' hoverable bordered={false}>

                            <div className="alignment">
                                <div className="mainText">
                                    <div className="smallCardTitle">
                                    <span>
                                        SYSTEM STATUS
                                    </span>
                                    </div>
                                    <div className="smallCardContent">
                                    <span>
                                        Running
                                    </span>
                                    </div>
                                </div>

                            </div>
                            <CloudFilled className="smallCardIcon"/>
                        </Card>
                    </Col>
                </Row>

                <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                    <Col className="dashboardCard" flex="auto">
                        <MarsLineChart/>
                    </Col>

                </Row>

                <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                    <Col className="dashboardCard" flex="auto">
                        <MarsLineChart/>
                    </Col>

                </Row>


            </Content>


        )

    }

}

export default DashboardMars;