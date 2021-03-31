import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom'
import Login from '../pages/login'
import Home from '../pages/home'

function RouterIndex() {
    return <Router>
        <Switch>
            <Route path="/login" component={Login}/>
            <Route path="/" component={Home}/>
        </Switch>
    </Router>
}
export default RouterIndex
