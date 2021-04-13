import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect,
    Link
} from 'react-router-dom'
import Login from '../pages/login'
import Home from '../pages/home'
import Register from '../pages/register'
import Error_404 from '../pages/error_404'
const routers = [
    {
        path:'/',
        component: Home
    },
    {
        path:'*',
        component: Error_404
    }
]

function render_router(routers) {
    return routers.map(({path,component})=>{
        return <Route path={path} component={component} />
    })
}
function RouterIndex(props) {
    return <Router>
        <Switch>
            <Route path="/login" component={Login}/>
            <Route path="/register" component={Register}/>
            {props.isLogin ?
                render_router(routers): <Redirect to="/login"/>
            }
        </Switch>
    </Router>
}

export default RouterIndex
