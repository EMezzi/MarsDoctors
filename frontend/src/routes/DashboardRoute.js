import React, {Component, useState} from 'react';
import axios from "axios";
import "../css/App.css"
import {Button, Card, Col, InputNumber, Row, Skeleton, Slider} from "antd";
import {Content} from "antd/es/layout/layout";
import {CloudFilled, DashboardOutlined, DislikeOutlined, LikeOutlined} from "@ant-design/icons";
import FeaturesCard from "../components/dashboard/featuresCard";
import DonutCard from "../components/dashboard/donutCard";
import GaugeCard from "../components/dashboard/gaugeCard";
import BulletCard from "../components/dashboard/bulletCard";
import DensityCard from "../components/dashboard/densityCard";
import PopoverHelp from "../components/dashboard/popoverHelp";

const riskCardTitlePopup = "Customize model sensitivity to fraud."
const riskCardContentPopup = "Use the slider below to change how sensitive the model is to potential fraudalent " +
    "transactions. Lower values for the threshold means more potential frauds will be caught while a higher value allows " +
    "the model to be more flexible blocking less transactions. You can use the other cards that display information about " +
    "the validation dataset to get a good idea of your preferred threshold when it comes to the sensitivity of the model."

// const riskCardContentPopup = <div>
//     Use the slider below to change how sensitive the model is to potential fraudalent
//     transactions. <br/> Lower values for the threshold means more potential frauds will be caught while a higher value allows
//     the model to be more flexible blocking less transactions.
//</div>
class DashboardRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            current_threshold: 0.39,
            total_transactions: 0,
            authorized_transactions: 0,
            blocked_transactions: 0,
            model_metrics: {}
        }

        this.loadData = this.loadData.bind(this)
        this.sendData = this.sendData.bind(this)
        this.loadStats = this.loadStats.bind(this)
        this.loadMetrics = this.loadMetrics.bind(this)
    }

    loadData() {

        const backEndUrl_threshold = 'http://127.0.0.1:8000/prediction_threshold/'
        const getBackendData = async () => {
            try {
                const data_threshold = await axios.get(backEndUrl_threshold);
                this.setState({current_threshold: data_threshold.data})
            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading threshold")
                //this.setState({loading: false})
            }
        };

        getBackendData()
    }

    loadMetrics() {

        const backEndUrl_stats = 'http://127.0.0.1:8000/model_metrics/'
        const getBackendData = async () => {
            try {

                const data_metrics = await axios.get(backEndUrl_stats);
                this.setState({
                    model_metrics: data_metrics.data
                })
            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading metrics")
                console.log(this.state.model_metrics)
                this.setState({loading: false})
            }
        };

        getBackendData()
    }

    loadStats() {

        const backEndUrl_stats = 'http://127.0.0.1:8000/data_stats/'
        const getBackendData = async () => {
            try {

                const data_stats = await axios.get(backEndUrl_stats);
                this.setState({
                    total_transactions: data_stats.data.total_transaction,
                    authorized_transactions: data_stats.data.authorized_transactions,
                    blocked_transactions: data_stats.data.blocked_transactions
                })
            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading stats")
                //this.setState({loading: false})
            }
        };

        getBackendData()
    }

    componentDidMount() {
        this.loadStats()
        this.loadData()
        this.loadMetrics()
    }


    componentDidUpdate(prevProps, prevState, snapshot) {

    }

    sendData(value) {

        const backEndUrl = 'http://127.0.0.1:8000/prediction_threshold?threshold=' + value

        const putBackendData = async () => {
            try {
                const data = await axios.put(backEndUrl);
                console.log(data.data)

            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Put complete")
                this.loadStats()
                this.loadMetrics()
                this.render()
                this.setState({loading: false})
            }
        };

        putBackendData()
    }


    render() {



        const DecimalStep = () => {
            const [inputValue, setInputValue] = useState(this.state.current_threshold);

            const onChange = (value) => {
                console.log(value)
                if (isNaN(value)) {
                    return;
                }
                setInputValue(value);
            };

            const onChange2 = (value) => {
                console.log(value)
                if (isNaN(value)) {
                    return;
                }
                setInputValue(value);

                this.setState({current_threshold: value}, () => {
                    this.sendData(value)
                });
            };

            const onClick = () => {

                this.setState({current_threshold: inputValue}, () => {
                    this.sendData(inputValue)
                });
            };

            const marks = {
                0: {
                    style: {
                        color: '#3f3939',
                        marginTop: 10,
                        marginLeft: 15
                    },
                    label: <strong>Less <br/> Fraud</strong>,
                },
                1: {
                    style: {
                        color: '#3f3939',
                        marginTop: 10,
                        marginLeft: -20,

                    },
                    label: <strong>More fraud</strong>,
                },
            };

            return (

                <Row style={{marginBottom:20}} gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                    <Col span={24} flex="auto">
                        <Slider
                            min={0}
                            max={1}
                            onChange={onChange}
                            onAfterChange={onChange2}
                            value={typeof inputValue === 'number' ? inputValue : 0}
                            step={0.01}
                            className="slider"
                            trackStyle={{backgroundColor:"lightgreen", height:10}}
                            railStyle={{backgroundColor: 'lightgrey', height:10}}
                            handleStyle={{ height:15, width:15, "margin-top": 2.5}}
                            markStyle={{ height:15, width:15, "margin-top": 2.5}}
                            marks={marks}

                        />
                    </Col>
                    <Col>
                        <InputNumber
                            min={0}
                            max={1}
                            style={{
                                margin: '0',
                            }}
                            step={0.01}
                            value={inputValue}
                            onChange={onChange}
                        />
                    </Col>

                    <Col>
                        <div style={{
                            margin: '0'
                        }}>
                            <Button type="primary" block onClick={onClick}>
                                Save
                            </Button>
                        </div>
                    </Col>

                </Row>
            );
        };

        return (
            <Content>
                <Skeleton active={true} loading={this.state.loading}>
                    <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                        <Col className="topCards" flex="auto">
                            <Card bodyStyle={{
                                height: '9vh'
                            }} className='transactionTest' hoverable bordered={false}>
                                <div className="alignment">
                                    <div className="mainText">
                                        <div className="smallCardTitle">
                                        <span>
                                            TOTAL TRANSACTIONS
                                        </span>
                                        </div>

                                        <div className="smallCardContent">
                                        <span>
                                            {this.state.total_transactions}
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
                                            AUTHORIZED TRANSACTIONS
                                        </span>
                                        </div>

                                        <div className="smallCardContent">
                                        <span>
                                            {this.state.authorized_transactions} ({(this.state.authorized_transactions /
                                            this.state.total_transactions * 100).toFixed(2)}%)
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
                                            BLOCKED TRANSACTIONS
                                        </span>
                                        </div>

                                        <div className="smallCardContent">
                                        <span>
                                            {this.state.blocked_transactions} ({(this.state.blocked_transactions /
                                            this.state.total_transactions * 100).toFixed(2)}%)
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
                            <Card className='sliderCard' hoverable title="Risk sensitivity tuning" bordered={false} extra={<PopoverHelp content={riskCardContentPopup} title={riskCardTitlePopup}/>}>

                                <DecimalStep/>

                                <BulletCard true_recall={this.state.model_metrics["True"]}/>

                            </Card>
                        </Col>
                    </Row>
                    <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                        <Col className="dashboardCard" span={12} flex="auto" >
                            <GaugeCard true_recall={this.state.model_metrics["True"]}/>
                        </Col>

                        <Col className="dashboardCard" span={12} flex="auto">
                            <FeaturesCard/>
                        </Col>
                    </Row>

                    <Row gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                        <Col className="dashboardCard"  flex="auto">
                            <DensityCard/>
                        </Col>
                    </Row>
                </Skeleton>

            </Content>


        )

    }


}

export default DashboardRoute;