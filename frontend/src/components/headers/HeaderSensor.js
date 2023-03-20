import React from 'react';
import {Button, Layout} from "antd";
import {DownloadOutlined} from "@ant-design/icons";


const {Header} = Layout;

/**
 * @author Matei
 * @version 0.1
 *
 * Header component for the quality metrics
 */
class HeaderSensor extends React.Component {

    render() {

        return (

            <div className="headerDash" style={{color: "darkslategray"}}>
                Sensor Simulation Page
            </div>

        );
    }

}

export default HeaderSensor;