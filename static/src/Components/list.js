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
              <h6 style={{ fontSize: "15px", color: "black" }}>'{blog.date}'</h6>
              <h6 style={{ fontSize: "25px" }}>{blog.title}</h6>

              <h6 style={{ fontSize: "30px", color: "black" }}>{blog.snippet}</h6>
              <h6 style={{ fontStyle: "italic", marginTop: "20px", fontSize: "20px" }}>{blog.author}</h6>
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

const snipp = {
  color: "black", fontSize: "23px",
  fontWeight: "normal"
};
const tit = {
  textDecoration: "none",
  fontSize: "20px"
};

function RenderStall({ blog }) {

  return (

    <div>
      <Link to={`/blog/${blog.id}`}>

        <div className="blog">

          <img src={blog.blogimg} alt="img" />

          <div className="desc" style={{ marginTop: "2px" }}>
            <h6 style={{ fontSize: "15px", color: "black" }}>'{blog.date}'</h6>
            <h6 style={tit}>{blog.title}</h6>

            <h6 style={snipp}>{blog.snippet}</h6>
            <h6 style={{ fontStyle: "italic", marginTop: "15px" }}>{blog.author}</h6>
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
    if (blog.featured) {
      return (


        <div key={blog.id}>

          <div> <RFeat blog={blog} /></div>

        </div>


      );
    }
  });
  console.log(props);
  const blogss = props.blogs.map((blog) => {
    if (!blog.featured) {
      return (


        <div key={blog.id}>


          <div><RenderStall blog={blog} /></div>


        </div>


      );
    }

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