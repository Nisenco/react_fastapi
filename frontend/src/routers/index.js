import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom'
import Login from '../pages/login'
import Home from '../pages/home'
import Register from '../pages/register'

function RouterIndex() {
    return <Router>
        <Switch>
            <Route path="/login" component={Login}/>
            <Route path="/register" component={Register}/>
            <Route path="/" component={Home}/>
        </Switch>
    </Router>
}
export default RouterIndex
