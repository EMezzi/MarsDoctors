import React from "react";
import {Button, Card, Popover} from "antd";
import {PoweroffOutlined, QuestionOutlined, SearchOutlined} from "@ant-design/icons";


class PopoverHelp extends React.Component {

    /**
     * Creates a new instance of this class with the initialized props
     * @param props:
     * currentFile - the current file selected in the dashboard
     */
    constructor(props) {
        super(props);

        this.state = {
            open: false
        }

    }

    componentDidMount() {

    }


    componentDidUpdate(prevProps, prevState, snapshot) {
    }

    render() {

        const hide = () => {
            this.setState({open: false})
        };

        const handleOpenChange = (newOpen) => {
            this.setState({open: newOpen})
        };

        return(
            <Popover
                content={this.props.content}
                title={this.props.title}
                trigger="click"
                open={this.state.open}
                onOpenChange={handleOpenChange}
            >
                <Button shape="circle" type="primary" icon={<QuestionOutlined />} />

            </Popover>
        )

    }


}

export default PopoverHelp