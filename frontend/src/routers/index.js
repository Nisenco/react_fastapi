import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect
} from 'react-router-dom'
import Login from '../pages/login'
import Register from '../pages/register'
import route_config from './router_config'

function render_router(routers) {
    return routers.map(({path, component,key}) => {
        return <Route key={key} path={path} component={component}/>
    })
}

function RouterIndex() {
    return <Router>
        <Switch>
            <Route path="/login" component={Login}/>
            <Route path="/register" component={Register}/>
            {render_router(route_config)}
        </Switch>
    </Router>
}

export default RouterIndex;
