import React from 'react';
import ReactHtmlParser from 'html-react-parser';
import { Card, CardImg, CardBody, CardText, CardTitle, } from 'reactstrap';



function RenderBlog({blog}  ) {
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


  return (
    <div>
      <RenderBlog blog={props.blog} />
    </div>

  );

}
export default BlogDetail;