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
class HeaderPredict extends React.Component {

    render() {

        return (

                <div className="headerDash" style={{color: "darkslategray"}}>
                    Notification history
                </div>

        );
    }

}

export default HeaderPredict;