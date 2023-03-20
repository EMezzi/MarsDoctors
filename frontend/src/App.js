import './css/App.css';
import SideBar from './components/menus/SiderMenu';
import React from 'react';
import {BrowserRouter, Route, Switch, Redirect,} from "react-router-dom"
import {FloatButton, Layout} from 'antd';
import HeaderDashboard from "./components/headers/HeaderDashboard";
import HeaderPredict from "./components/headers/HeaderPredict";
import HistoryRoute from "./routes/HistoryRoute";
import DashboardMars from "./routes/DashboardMars";
import SensorRoute from "./routes/SensorRoute";
import HeaderSensor from "./components/headers/HeaderSensor";

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
