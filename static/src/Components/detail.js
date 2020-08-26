import React from 'react';
import ReactHtmlParser from 'html-react-parser';
import { Card, CardImg, CardBody, CardText, CardTitle, } from 'reactstrap';
import { Loading } from './LoadingComponent';


function RenderBlog({ blog }) {
  return (
    <div>
      {/* class="imb" */}

                  
                      <img src={blog.blogimg} alt="img" />
                  

      <div className="written">
        {/* <p>{blog.content}</p> */}
       { ReactHtmlParser(blog.content)}
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