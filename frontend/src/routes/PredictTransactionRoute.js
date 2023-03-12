import React, {Component} from 'react';
import {Card, Row, Col, Input, Button} from "antd";
import "../css/App.css"
import axios from "axios";
import PopoverHelp from "../components/dashboard/popoverHelp";

const { TextArea } = Input;

const defaultTransaction = "{\n" +
    "  \"psp_reference\": 30568848810,\n" +
    "  \"merchant\": \"Merchant B\",\n" +
    "  \"card_scheme\": \"MasterCard\",\n" +
    "  \"year\": 2021,\n" +
    "  \"hour_of_day\": 12,\n" +
    "  \"minute_of_hour\": 46,\n" +
    "  \"day_of_year\": 301,\n" +
    "  \"is_credit\": false,\n" +
    "  \"eur_amount\": 302.8,\n" +
    "  \"ip_country\": \"BR\",\n" +
    "  \"issuing_country\": \"BR\",\n" +
    "  \"device_type\": \"Android\",\n" +
    "  \"ip_address\": \"lrv121gcxicRXmTi\",\n" +
    "  \"email_address\": \"lrv4cicRXmTi-Bq1MLCDZw\",\n" +
    "  \"card_number\": \"1uiQZx3IboDm1rnoeZH9sw\",\n" +
    "  \"shopper_interaction\": \"Ecommerce\",\n" +
    "  \"zip_code\": \"FFR\",\n" +
    "  \"card_bin\": 4645\n" +
    "}"

const titleHelp = "Simulate sending a new transaction to our backend API and ML model."
const contentHelp = "By filling in the data of a new transaction, you can simulate sending it to our API and machine " +
    "learning model where our code will process it and return the probabilities of it being fraudulent or not."

class PredictTransactionRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            transaction: defaultTransaction,
            loading: false,
            response: null,
            time: 0
        }

        this.processTransaction = this.processTransaction.bind(this)
    }


    /**
     * On component did mount we make the API call for the data.
     */
    componentDidMount() {
        console.log("Component loaded")
    }

    /**
     * Sets the new state of the current file
     */
    async processTransaction() {

        const backEndUrl = 'http://127.0.0.1:8000/process_transaction/'
        const start = Date.now()
        const data = await axios.post(backEndUrl, this.state.transaction, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        this.setState({loading: true})

        console.log(data.data)
        this.setState({response: JSON.stringify(data.data)})
        //await new Promise(r => setTimeout(r, 200));
        const end = Date.now();
        this.setState({time: end-start})
        this.setState({loading: false})
    }


    render() {

        return (
            <Row>
                <Col span={24}>
                    <Card className='transactionTest' hoverable title="Send a transaction to the API" bordered={false} extra={<PopoverHelp title={titleHelp} content={contentHelp}/>}>
                        <div className="transactionInput">
                            <TextArea rows={21} defaultValue={defaultTransaction} onChange={(event) => this.setState({transaction: event.target.value})}  />
                        </div>

                        <div className="transactionButton" >
                            <Button type="primary" block onClick={this.processTransaction}>
                                Execute
                            </Button>
                        </div>


                        <div className="transactionStatus">
                            {this.state.loading ? "loading..." : this.state.response} {this.state.response ?
                            "Request took " + this.state.time + " milliseconds" : this.state.response}
                        </div>

                    </Card>
                </Col>
            </Row>

        )

    }


}

export default PredictTransactionRoute;