import './css/App.css';
import SideBar from './components/menus/SiderMenu';
import React from 'react';
import {BrowserRouter, Route, Switch, Redirect,} from "react-router-dom"
import {FloatButton, Layout, notification} from 'antd';
import HeaderDashboard from "./components/headers/HeaderDashboard";
import HeaderPredict from "./components/headers/HeaderPredict";
import HistoryRoute from "./routes/HistoryRoute";
import DashboardMars from "./routes/DashboardMars";
import SensorRoute from "./routes/SensorRoute";
import HeaderSensor from "./components/headers/HeaderSensor";
import axios from "axios";

/**
 * @author Matei
 * @version 0.1
 *
 * Main App class for the React application. This is where we load the most important components and we do the routing.
 * We use the Ant Design library for the dashboard layout and components and for the routing we use React-route.
 * More information about can be found at : https://ant.design/
 */

const {Content, Footer} = Layout;

// We try to keep our main App component based so that if we want to change certain aspects of our page all we have
//to do is just load a new component and not change any more code in here
class App extends React.Component {

  async checkBackendCycles() {
    try {
      const data_notifications = await axios.get("http://127.0.0.1:8000/cycle_complete/");
      if (data_notifications.data.status !== "No cycle is ready, there is nothing new to see.") {
        notification.info({
          message: data_notifications.data.type +  ' check complete!',
          description:
          data_notifications.data.status,
          duration: 0,
        });
      }
      // this.setState({data: data_notifications.data})
    } catch (err) {
      // Handle Error Here
      console.error(err);
    } finally {
      console.log("Checked for cycle complete")
    }
  }

  componentDidMount() {
    // Make the initial API call
    this.checkBackendCycles();

    // Set an interval to make the API call every 10 seconds
    setInterval(this.checkBackendCycles, 10000);
  }

  render() {

    return (
        /*We are using the BrowserRouter to create routes for the pages*/
        <BrowserRouter >
          <FloatButton.BackTop visibilityHeight={50}/>
          <Layout >
            {/*Load the Sidebar component*/}
            <SideBar/>

            <Layout className="site-layout">

              {/* Load correct header*/}
              <Switch>
                <Route path="/dashboard" component={HeaderDashboard}/>
                <Route path="/history" component={HeaderPredict}/>
                <Route path="/sensor" component={HeaderSensor}/>
                <Redirect to="/dashboard"/>
              </Switch>

              <Content style={{margin: '0 16px'}}>
                {/*Load correct page*/}
                <Switch>
                  <Route path="/dashboard" component={DashboardMars}/>
                  <Route path="/history" component={HistoryRoute}/>
                  <Route path="/sensor" component={SensorRoute}/>
                  <Redirect to="/dashboard"/>
                </Switch>
              </Content>

              <Footer style={{textAlign: 'center'}}>Complex Systems 2023</Footer>
            </Layout>



          </Layout>

        </BrowserRouter>



    );
  }
}


export default App;
