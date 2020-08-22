import React, { Component } from 'react';
import { Media } from 'reactstrap';

function RenderContent(blogC) {
    return (

        <div>
            <h1>Hello this is blog {blogC.id}</h1>
        </div>
    )
}

export default RenderContent;