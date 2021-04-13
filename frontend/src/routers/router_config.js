import Home from "../pages/home";
import Error_404 from "../pages/error_404";

const route_config = [
    {
        path:'/',
        component: Home
    },
    {
        path:'*',
        component: Error_404
    }
]
export default  route_config