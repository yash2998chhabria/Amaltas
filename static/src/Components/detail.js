import React from 'react';
import ReactHtmlParser from 'html-react-parser';
import { Card, CardImg, CardBody, CardText, CardTitle, } from 'reactstrap';



function RenderBlog({ blog }) {
  return (
    <div>
      <div className="cont">
        <div className="bloghead">
          <div className="desc2">
            <a href="./blog.html" style={{ textDecoration: "none" }}>
              <h6 style={{ fontSize: "25px" }}>Lorem ipsum, dolor sit amet consectetur .</h6>
            </a>
            <h6 style={{ fontSize: "30px", color: "black" }}>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Provident quia perferendis</h6>
            <h6 style={{ fontStyle: "italic", marginTop: "20px", fontSize: "20px" }}>Author</h6>
          </div>
        </div>
        <div class="imb">
          <img src={"https://learnwebcode.github.io/json-example/images/cat-2.jpg"} alt="img" />
        </div>
        {/* <Card>

        <CardImg top width="100%" src="" alt="Card image cap" />
        <CardBody>
          <CardTitle>{blog.title}</CardTitle>
          <CardText>{ReactHtmlParser(blog.content)}</CardText>
        </CardBody>

      </Card>
      {ReactHtmlParser(blog.content)} */}
      </div>
      <div className="written">
        <p>You’re just getting started with your online business efforts. Maybe it’s your first website, maybe you’re
        just now considering adding advertising efforts. Whatever your level of expertise, it’s probably safe to say
        you’re not an industry-leader when it comes to the advertising category. You’ll probably want to hire
        someone who actually is to help you get ahead like an advertising agency. But is that really necessary?
        Probably not. We break down when to tackle digital advertising yourself and when not to.

        <h6 style={{ fontSize: "35px", color: "black" }}>Why digital advertising is so important</h6>

        For some, having a website with contact information is enough. But for most, we would argue it isn’t. A
        website is a good start for a freelancer or small business owner who needs to be found online. A portfolio
        or place to look you up. But unless you’re engaged in a very niche industry, you probably have quite a lot
        of competitors who are fighting with you to get the same clients’ attention. That’s where digital
        advertising can really help boost your efforts.

        Digital advertising isn’t just putting up a Facebook and hoping for the best. It’s targeted, data-driven
        advertising strategy with the purpose of reaching leads and potential customers in every stage of the buying
        process and moving them closer to making a sale. Digital advertising efforts don’t cost an arm and a leg and
        will quickly get you more customers.

        Once you have a website set up, adding digital marketing and advertising solutions is easy - especially if
        you choose to do it through Cobiro, a central platform that combines your website and digital marketing.</p>
      </div>
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