import React, {useState, useEffect} from 'react';
import {Layout, Menu, Breadcrumb} from "antd";
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {
    DesktopOutlined,
    PieChartOutlined,
    FileOutlined,
    TeamOutlined,
    UserOutlined,
} from '@ant-design/icons';

const {Header, Content, Footer, Sider} = Layout;
const {SubMenu} = Menu;

function LayoutIndex(props) {
    const {layoutProps} = props;
    useEffect(() => {
        if (!layoutProps.isLogin) {
            props.history.push('/login');
        }
    }, [layoutProps.isLogin])
    const [collapsed, SetCollapsed] = useState(false);
    const onCollapse = collapsed => {
        console.log(collapsed);
        SetCollapsed(collapsed)
    };
    return (<div className="layout-container">
        <Layout style={{minHeight: '100vh'}}>
            <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
                <div className="logo"/>
                <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
                    <Menu.Item key="1" icon={<PieChartOutlined/>}>
                        Option 1
                    </Menu.Item>
                    <Menu.Item key="2" icon={<DesktopOutlined/>}>
                        Option 2
                    </Menu.Item>
                    <SubMenu key="sub1" icon={<UserOutlined/>} title="User">
                        <Menu.Item key="3">Tom</Menu.Item>
                        <Menu.Item key="4">Bill</Menu.Item>
                        <Menu.Item key="5">Alex</Menu.Item>
                    </SubMenu>
                    <SubMenu key="sub2" icon={<TeamOutlined/>} title="Team">
                        <Menu.Item key="6">Team 1</Menu.Item>
                        <Menu.Item key="8">Team 2</Menu.Item>
                    </SubMenu>
                    <Menu.Item key="9" icon={<FileOutlined/>}>
                        Files
                    </Menu.Item>
                </Menu>
            </Sider>
            <Layout className="site-layout">
                <Header className="site-layout-background" style={{padding: 0}}>
                    <div style={{float: 'right', color: 'white', marginRight: 20}}>Nicosen</div>
                </Header>
                <Content style={{margin: '0 16px'}}>
                    {/*<Breadcrumb style={{margin: '16px 0'}}>*/}
                    {/*    <Breadcrumb.Item>User</Breadcrumb.Item>*/}
                    {/*    <Breadcrumb.Item>Bill</Breadcrumb.Item>*/}
                    {/*</Breadcrumb>*/}
                    {/*<div className="site-layout-background" style={{padding: 24, minHeight: 360}}>*/}
                    {/*    Bill is a cat.*/}
                    {/*</div>*/}
                    {props.children}
                </Content>
                <Footer style={{textAlign: 'center'}}>Ant Design ©2021Created by Nicosen</Footer>
            </Layout>
        </Layout>
    </div>)
}

const mapStateToProps = (state) => {
    return {layoutProps: state.loginReducer}
}
export default withRouter(connect(mapStateToProps)(LayoutIndex))
