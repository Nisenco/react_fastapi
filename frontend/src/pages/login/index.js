import React from 'react';
import {Button, Form, Input, Checkbox,message} from 'antd';
import {connect} from 'react-redux';
import{withRouter} from 'react-router';
import axios from 'axios';
import './login.scss'


function Login(props) {
    console.log(props);
    const {setLoginStatus} = props
    const layout = {
        labelCol: {span: 7},
        wrapperCol: {span: 17},
    };
    const handleSubmit = (values)=>{
        axios.post('http://localhost:8008/api/login',{
            username:values.username,
            password:values.password
        }).then(({data:{status,msg}}) => {
            if(status == 200){
                setLoginStatus({isLogin:true});
                props.history.push('/');
            }else {
                message.error(msg);
            }
        })
    }
    const tailLayout = {
        wrapperCol: {offset: 7, span: 17},
    };
    const onFinish = (values) => {
        handleSubmit(values);
    };
    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };
    return (<div className="login-container">
        <div className="login-form">
            <div className="login-title">
                <h3>X管理系统</h3>
            </div>
            <Form
                {...layout}
                name="basic"
                initialValues={{remember: true}}
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
            >
                <Form.Item
                    name="username"
                    rules={[{required: true, message: 'Please input your username!'}]}
                >
                    <Input  placeholder="登录用户名/邮箱"/>
                </Form.Item>

                <Form.Item
                    name="password"
                    rules={[{required: true, message: 'Please input your password!'}]}
                >
                    <Input.Password placeholder="密码"/>
                </Form.Item>

                <Form.Item name="remember" valuePropName="checked">
                    <Checkbox>Remember me</Checkbox>
                </Form.Item>

                <Form.Item {...tailLayout}>
                    <Button type="primary" htmlType="submit">
                        登录
                    </Button>
                </Form.Item>
                <Form.Item>
                    没有账户，
                    <span
                        className="to-register"
                        onClick={()=>props.history.push('/register')}
                    >立即注册</span>
                </Form.Item>
            </Form>
        </div>
    </div>)
}

const mapStateToProps = (state)=>{
    return state.loginReducer;
}
const mapDispatchToProps = (dispatch)=>{
    return {
        setLoginStatus: payload=>dispatch({type:'SET_LOGIN',payload}),
    }
}
export default withRouter(connect(mapStateToProps,mapDispatchToProps)(Login))