import React from 'react'
import { Card, CardImg, CardBody, CardText, CardTitle, Button } from 'reactstrap';
import { Link } from 'react-router-dom'
import { Loading } from '../Components/LoadingComponent'

function RenderStall({ blog }) {
  return (
    <div>
      <Card>
        <Link to={`/blog/${blog.id}`}>
          <CardImg top width="100%" src="/assets/318x180.svg" alt="Card image cap" />
          <CardBody>
            <CardTitle>{blog.id}</CardTitle>
            <CardText>{blog.content}</CardText>
            <Button>Visit</Button>
          </CardBody>
        </Link>
      </Card>
    </div>
  );

}


const BlogList = (props) => {

  const blogss = props.blogs.map((blog) => {
    return (
      <div className="col-12 col-md-5 m-1" key={blog.id}>
        <RenderStall blog={blog} />
      </div>
    );
  });

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

    <div className="container">
      <div className="row">
        {blogss}
      </div>
    </div>
  )
}

export default BlogList