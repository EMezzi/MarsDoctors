import React from 'react';
import {Button, Layout} from "antd";
import "../../css/App.css"
import {DownloadOutlined} from "@ant-design/icons";


const {Header} = Layout;
/**
 * @author Matei
 * @version 0.1
 *
 * Header component for the privacy metrics
 */
class HeaderDashboard extends React.Component {

    render() {

        return(
                <div className="headerDash" style={{color: "darkslategray"}}>
                    MarsLife Health and Habitat Monitoring Dashboard

                    <Button style={{float:"right", marginRight: 15}} type="primary" shape="round" icon={<DownloadOutlined />} size={"default"}>
                        Download
                    </Button>
                </div>


        );
    }

}

export default HeaderDashboard;