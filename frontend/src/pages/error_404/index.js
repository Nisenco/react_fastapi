import React from 'react';
import {Button} from 'antd';
import './error_404.scss'
import img_404 from '../../assets/images/404.jpg';

function error_404(props){
    return <div className="container_404">
        <img src={img_404} />
    </div>
}

export default error_404