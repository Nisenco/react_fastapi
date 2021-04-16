import React from 'react';
import {Provider} from 'react-redux'
import './App.css';
import RouterIndex from "./routers";
import store from "./store";
const appState = store.getState();
const {loginReducer} = appState;
let {isLogin} = loginReducer;
console.log(isLogin,'app++++++___');
function App() {
    return (
        <Provider store={store}>
            <div className="App header">
                <RouterIndex isLogin={isLogin}/>
            </div>
        </Provider>
    );
}

export default App;
