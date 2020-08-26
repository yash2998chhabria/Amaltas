import React from 'react';
import ReactHtmlParser from 'html-react-parser';
import { Card, CardImg, CardBody, CardText, CardTitle, } from 'reactstrap';
import { Loading } from './LoadingComponent';

const blohim = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
}
const intim = {
  height: "210px",
  width: "240px",
  margin: "5px",
}
function RenderBlog({ blog }) {
  return (
    <div>
      {/* class="imb" */}

      <div className="cont">
        <div className="bloghead">
          <div className="desc2">
            <h6 style={{ fontSize: "15px", color: "black" }}>{blog.date}</h6>
            <h6 style={{ textDecoration: "none", fontSize: "27px" }}>{blog.title}</h6>
            <h6 style={{ fontSize: "30px", color: "black" }}>{blog.snippet}</h6>
            <h6 style={{ fontStyle: "italic", marginTop: "20px", fontSize: "20px" }}>Author</h6>
          </div>
        </div>
        <div style={blohim}>
          <img src={blog.blogimg} style={intim} alt="img" />
        </div>
      </div>

      <div className="written">
        {/* <p>{blog.content}</p> */}
        {ReactHtmlParser(blog.content)}
      </div>
    </div>
  )
}




const BlogDetail = (props) => {
  console.log(props.blog)

  if (props.blogLoading) {
    return (

      <Loading />

    );
  } else if (props.blogErrMess) {
    return (
      <div className="container">
        <div className="row">
          <div className="col-12">
            <h4>{props.dishes.errMess}</h4>
          </div>
        </div>
      </div>
    );
  } else
    return (
      <div>
        <RenderBlog blog={props.blog} />
      </div>

    );

}
export default BlogDetail;