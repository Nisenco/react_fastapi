import React, {useState} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import LayoutIndex from '../layout';
import {Button} from 'antd';
import './home.scss'

function Home(props) {
    const [count, setCount] = useState(0);
    return <div className="home-container">
        <LayoutIndex>
            <div>{count}</div>
            <Button onClick={() => setCount(count + 1)}>increase</Button>
            <Button onClick={() => setCount(count - 1)}>decrease</Button>
        </LayoutIndex>
    </div>
}

const mapStateToProps = (state) => {
    return state.homeReducer
};
const mapDispatchToProps = () => {
    return {}
};
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Home))