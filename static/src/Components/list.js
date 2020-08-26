import React from 'react'
import { Card, CardImg, CardBody, CardText, CardTitle, Button } from 'reactstrap';
import { Link } from 'react-router-dom'
import { Loading } from '../Components/LoadingComponent'




function RenderStall({ blog }) {
  return (

    <div>
      <Link to={`/blog/${blog.id}`}>

        <div className="blog">
          <img src={"https://learnwebcode.github.io/json-example/images/cat-2.jpg"} alt="img" />
          <div className="desc" style={{ marginTop: "2px" }}>
            <h6 style={{ fontSize: "15px" }}>26/07/1999</h6>
            <h6 style={{ textDecoration: "none", fontSize: "17px" }}>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Pr</h6>

            <h6 style={{ color: "black", fontSize: "22px", fontWeight: "normal" }}>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Provident quia perferendis</h6>
            <h6 style={{ fontStyle: "italic", marginTop: "15px" }}>Author</h6>
          </div>
        </div>

      </Link>
    </div>




  )

}


const BlogList = (props) => {
  // const FeatB = props.blogs.filter((data) => {
  //   data.id === 6; return (
  //     <div></div>
  //   )
  // })[0];


  console.log(props);
  const blogss = props.blogs.map((blog) => {

    return (
      <div>

        <div key={blog.id}>
          <RenderStall blog={blog} />
        </div>

      </div>
    );
  });



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
  }

  else
    return (


      <div className="cont">
        {/* {FeatB} */}
        {blogss}
      </div>

    )

}



export default BlogList