import React from 'react';
import ReactHtmlParser from 'html-react-parser';
import { Card, CardImg, CardBody, CardText, CardTitle, } from 'reactstrap';



function RenderBlog({ blog }) {
  return (
    <div className="col-12 col-md-5 m-1" >
      <Card>

        <CardImg top width="100%" src="" alt="Card image cap" />
        <CardBody>
          <CardTitle>{blog.title}</CardTitle>
          <CardText>{ReactHtmlParser(blog.content)}</CardText>
        </CardBody>

      </Card>
      {/* {ReactHtmlParser(blog.content)} */}
    </div>
  )
}




const BlogDetail = (props) => {
  console.log(props.blog)

  if (props.blogLoading) {
    return (
      <div className="container">
        <div className="row">
          <Loading />
        </div>
      </div>
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