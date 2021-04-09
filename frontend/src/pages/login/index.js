import React, {useContext, createContext, useState,useEffect} from 'react'
import {Button, Form, Input, Checkbox} from 'antd'
import axios from 'axios';
import './login.scss'


function Index(props) {
    console.log('props=>', props);
    const layout = {
        labelCol: {span: 7},
        wrapperCol: {span: 17},
    };
    // const handleSubmit = ()=>{
    //     axios.post('http://localhost:8008/users/login', )
    // }
    const tailLayout = {
        wrapperCol: {offset: 7, span: 17},
    };
    const onFinish = (values) => {
        console.log('Success:', values);
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
                    rules={[{required: true, message: 'Please input your username!'}]}
                >
                    <Input  placeholder="登录用户名/邮箱"/>
                </Form.Item>

                <Form.Item
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
                        class="to-register"
                        onClick={()=>props.history.push('/register')}
                    >立即注册</span>
                </Form.Item>
            </Form>
        </div>

    </div>)
}

export default Index