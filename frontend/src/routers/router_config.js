import Home from "../pages/home";
import Error_404 from "../pages/error_404";

const route_config = [
    {
        path:'/',
        key:'home',
        component: Home
    },
    {
        path:'*',
        key:'error_404',
        component: Error_404
    }
]
export default  route_config