import React from 'react';

export const Loading = () => {
    return (

        <div className="load" style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
            <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
            <p style={{ marginTop: "20px", marginLeft: "5px" }}></p>

        </div>
    );
};