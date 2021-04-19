import React from 'react';
import {Provider} from 'react-redux'
import './App.css';
import RouterIndex from "./routers";
import store from "./store";
function App() {
    return (
        <Provider store={store}>
            <div className="App header">
                <RouterIndex />
            </div>
        </Provider>
    );
}

export default App;
