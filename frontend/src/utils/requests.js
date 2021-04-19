import axios from 'axios';
import store from '../store';
const stores = store.getState();
console.log(stores,'req=====');

//axios 默认配置

axios.defaults.baseURL = 'http://localhost:8008/api/';
axios.defaults.timeout = 5000;
axios.interceptors.request.use(
    config => {
        return config
    },
    err => {
        return Promise.reject(err)
    },
);
// http response 拦截器
axios.interceptors.response.use(
    response => {
        return response
    },
    error => {
        return Promise.reject(error.response.data)
    },
)

export default axios;