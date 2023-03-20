import React from 'react';
import logo from "../../resources/logo.png";
import {Layout, Menu} from "antd";
import {CreditCardOutlined, DashboardOutlined, WifiOutlined} from "@ant-design/icons";
import {Link} from "react-router-dom";
import {withRouter} from "react-router";
import '../../css/App.css';

const {Sider} = Layout;

/**
 * @author Matei
 * @version 0.1
 *
 * This Component represents the sidebar where the Menu resides. We use it from the Ant design library. It is responsive
 * to the screen width and it minimizes. It uses history paths to keep track of the selected path everytime.
 *
 * Theme can be set to dark or white so can be the size of the minimization.
 */
class SiderMenu extends React.Component {

    // Menu defaults to the quality metrics page, dark theme by default and it is set to not collapses
    state = {
        collapsed: false,
        theme: 'dark',
        current: '/dashboard',
    };


    // On click sets the current page
    handleClick = e => {
        this.setState({
            current: e.key,
        });
    };

    render() {
        // We keep a queue of histories in order to be able to backtracking when the user goes back to a previous
        // page we can know what page it is.
        const {history} = this.props;

        return (
            <Sider
                breakpoint="lg"
                collapsedWidth="80"
                collapsedHeigth="200"
            >
                <div className="sider-top">
                    {/*Company logo and name*/}
                    <Link to="/dashboard">
                        <img className="App-logo" alt={"Agyen logo"} src={logo}/>
                    </Link>
                </div>

                <Menu theme={this.state.theme}
                      onClick={this.handleClick}
                      style={{minHeight: '100vh'}}
                      defaultOpenKeys={['/1']}
                      selectedKeys={[history.location.pathname]}
                      mode="inline">

                    <Menu.Item key="/dashboard" icon={<DashboardOutlined />}>
                        <Link to="/dashboard"/>
                       Dashboard
                    </Menu.Item>
                    <Menu.Item key="/history" icon={<CreditCardOutlined /> }>
                        <Link to="/history"/>
                        Notifications
                    </Menu.Item>
                    <Menu.Item key="/sensor" icon={<WifiOutlined />}>
                        <Link to="/sensor"/>
                        Sensor Test
                    </Menu.Item>

                </Menu>

            </Sider>
        );
    }


}

export default withRouter(SiderMenu);
