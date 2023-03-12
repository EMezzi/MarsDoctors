import React, {useState} from "react";
import {Col, InputNumber, Row, Slider, Card, Button} from 'antd';
import axios from "axios";

/**
 *
 */
class SliderCard extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            current_threshold: 0,

        }

        this.loadData = this.loadData.bind(this)
        this.sendData = this.sendData.bind(this)

    }

    loadData() {

        const backEndUrl = 'http://127.0.0.1:8000/prediction_threshold/'
        const getBackendData = async () => {
            try {
                const data = await axios.get(backEndUrl);
                this.setState({current_threshold: data.data})
                console.log(data.data)

            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading threshold")
                this.setState({loading: false})
            }
        };

        getBackendData()
    }

    componentDidMount() {
        this.loadData()
    }


    componentDidUpdate(prevProps, prevState, snapshot) {
        // This component probably doesn't change
    }

    sendData(value) {

        const backEndUrl = 'http://127.0.0.1:8000/prediction_threshold?threshold=' + value

        //console.log("Current value in props is", this.state.current_threshold)
        //console.log("new value sent is", value)

        const putBackendData = async () => {
            try {
                const data = await axios.put(backEndUrl);
                //this.setState({model_features: data.data})
                console.log(data.data)

            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Put complete")
                //this.setState({loading: false})
            }
        };

        putBackendData()
    }


    render() {

        const marks = {
            0: '0°C',
            26: '26°C',
            37: '37°C',
            1: {
                style: {
                    color: '#f50',
                },
                label: <strong>100°C</strong>,
            },
        };

        const DecimalStep = () => {
            const [inputValue, setInputValue] = useState(this.state.current_threshold);

            const onChange = (value) => {
                if (isNaN(value)) {
                    return;
                }
                setInputValue(value);
            };

            const onClick = () => {

                this.setState({current_threshold: inputValue}, () => {
                    console.log("a", this.state.current_threshold)
                    this.sendData(inputValue)
                });
            };
            return (
                <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
                    <Col span={12} flex="auto">
                        <Slider
                            min={0}
                            max={1}
                            onChange={onChange}
                            value={typeof inputValue === 'number' ? inputValue : 0}
                            step={0.01}
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
                        }} >
                            <Button type="primary" block onClick={onClick}>
                                Save
                            </Button>
                        </div>
                    </Col>

                </Row>
            );
        };

        return(
            <Card  className='sliderCard' hoverable title="Model tuning" bordered={false}>
                <DecimalStep />
            </Card>
        )

    }


}

export default SliderCard