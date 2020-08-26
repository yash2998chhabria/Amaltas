import React from 'react'
import { Link } from 'react-router-dom'


function RenderFeat({ dishes }) {
    // console.log(dishes)
    return (
        <div>

            <Link to={`/blog/${dishes}`}>
                <div className="cont" style={{ marginBottom: "90px" }}>
                    <div className="bloghead">
                        <div className="desc2">
                            <a href="./blog.html" style={{ textDecoration: "none" }}>
                                <h6 style={{ fontSize: "25px" }}>Lorem ipsum, Featured dolor sit amet consectetur .</h6>
                            </a>
                            <h6 style={{ fontSize: "30px", color: "black" }}>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Provident quia perferendis</h6>
                            <h6 style={{ fontStyle: "italic", marginTop: "20px", fontSize: "20px" }}>Author</h6>
                        </div>
                    </div>
                    <div class="imb">
                        <img src={"https://learnwebcode.github.io/json-example/images/cat-2.jpg"} alt="img" />
                    </div>
                </div>
            </Link>

        </div>
    )
}

const FeatBlog = ({ dishes }) => {
    console.log(dishes);
    return (
        <RenderFeat dishes={dishes} />
    )
}


export default FeatBlog;