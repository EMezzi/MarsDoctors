import React, {Component} from 'react';
import axios from "axios";
import {Skeleton} from "antd";


class PredictRoute extends Component {

    // Initializes the class and sets the default values for the state.
    constructor(props) {
        super(props);

        this.state = {
            accuracy: 0,
            loading: true,
            precision: 0
        }
    }

    /**
     * Async method that calls the backend and retrieves the current projects for the current user. On finalization of
     * the call sets the loading status of the page to false which triggers the rendering of the actual quality.
     */
    loadData() {

        const backEndUrl = 'http://127.0.0.1:8000/model_metrics/'
        const getBackendData = async () => {

            try {
                const data = await axios.get(backEndUrl);
                this.setState({accuracy: data.data})
                this.setState({precision: data.data.macro_avg.precision})
                console.log(data.data.macro_avg.precision)
                console.log(this.state.accuracy)
            } catch (err) {
                // Handle Error Here
                console.error(err);
            } finally {
                console.log("Done loading data")
                this.setState({loading: false})
            }
        };

        getBackendData()
    }

    /**
     * On component did mount we make the API call for the data.
     */
    componentDidMount() {
        this.loadData()
    }

    render() {

        return (
            <Skeleton active={true} loading={this.state.loading}>
                <div>
                    Accuracy is {this.state.accuracy.accuracy}, and precision is {this.state.precision}
                </div>
            </Skeleton>

        )

    }


}

export default PredictRoute;