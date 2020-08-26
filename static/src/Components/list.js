import React from 'react'
import { Card, CardImg, CardBody, CardText, CardTitle, Button } from 'reactstrap';
import { Link } from 'react-router-dom'
import { Loading } from '../Components/LoadingComponent'

function RFeat({ blog }) {
  return (
      <div>

          <Link to={`/blog/${blog.id}`}>
              <div className="cont" style={{ marginBottom: "90px" }}>
                  <div className="bloghead">
                      <div className="desc2">
                          <a href="./blog.html" style={{ textDecoration: "none" }}>
                              <h6 style={{ fontSize: "25px" }}>{blog.Title}.</h6>
                          </a>
  <h6 style={{ fontSize: "30px", color: "black" }}>{blog.snippet}</h6>
                          <h6 style={{ fontStyle: "italic", marginTop: "20px", fontSize: "20px" }}>Author</h6>
                      </div>
                  </div>
                  <div class="imb">
                      <img src={blog.blogimg} alt="img" />
                  </div>
              </div>
          </Link>

      </div>
  )
}


function RenderStall({ blog }) {
  
  return (
    
    <div>
      <Link to={`/blog/${blog.id}`}>

        <div className="blog">
          <img src={blog.blogimg} alt="img" />
         
          <div className="desc" style={{ marginTop: "2px" }}>
            <h6 style={{ fontSize: "15px" }}>{blog.date}</h6>
  <h6 style={{ textDecoration: "none", fontSize: "17px" }}>{blog.title}</h6>

            <h6 style={{ color: "black", fontSize: "22px", fontWeight: "normal" }}>{blog.snippet}</h6>
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

  const feat = props.blogs.map((blog) => {
    if(blog.featured){
    return (
      

        <div key={blog.id}>
          
          <div> <RFeat blog={blog} /></div>
         
        </div>

      
    );}
  });
  console.log(props);
  const blogss = props.blogs.map((blog) => {
    if(!blog.featured){
    return (
    

        <div key={blog.id}>
        
         
          <div><RenderStall blog={blog} /></div>
         
          
        </div>

     
    );}

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

<div>
        {feat}
      <div className="cont">
        {blogss}
      </div>
      </div>
    )

}



export default BlogList