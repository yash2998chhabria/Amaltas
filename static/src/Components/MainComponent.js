import React, { Component } from 'react';
import { Media } from 'reactstrap';
//import axios from 'axios';
import { baseUrl } from '../shared/baseUrl';
import { connect } from 'react-redux';
import { fetchDishes } from '../redux/ActionCreators';
import { Loading } from './LoadingComponent';
import BlogList from './list'
import BlogDetail from './detail'
import { Switch, Route,  withRouter } from "react-router-dom";
import Home from './HomeComponent';

const mapStateToProps = state => {
    return {
        dishes: state.dishes,
    }
  }
  const mapDispatchToProps = dispatch => ({
  
    fetchDishes: () => { dispatch(fetchDishes()) }
  
  });

class Main extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [
                {
                "id": 1,
                "title": "cncn",
                "content": "<h1>snc ns fnnnnd ndndd ddd djndvndk dvllsv</em></h1>"
            },
            {
                "id": 2,
                "title": "hsvhufshufuz",
                "content": "snvjsnjs"
            },
            {
                "id": 3,
                "title": "hsvhufshufuz",
                "content": "snvjsnjs"
            }],
            
        }
    }   
    // componentDidMount() {
    //     axios.get('http://127.0.0.1:8000/api/article/')
    //     .then(res => { this.setState({
    //         list: res.data
    //     }) })
    //     .catch(err => { this.setState({error: err})})
    //     console.log(list)
    // }
    componentDidMount() {
        this.props.fetchDishes();
        // fetch(baseUrl + 'api/article/')
        // .then(res => res.json())
        // .then((data) => {
        //   this.setState({ list : data })
        //   console.log(this.state.list)
        // })
        // .catch(console.log)
      }        
    

    // render() {
    //     const menu = this.props.dishes.dishes.map((dish) => {
    //         return (
    //           <div key={dish.id} className="col-12 mt-5">
    //             <Media tag="li">
    //               <Media left middle>
    //                   <Media object src={dish.image} alt={dish.name} />
    //               </Media>
    //               <Media body className="ml-5">
    //                 <Media heading>{dish.name}</Media>
    //                 <p>{dish.description}</p>
    //               </Media>
    //             </Media>
    //           </div>
    //         );
    //     });

    //     if (this.props.dishes.isLoading) {
    //         return (
    //           <div className="container">
    //             <div className="row">
    //               <Loading />
    //             </div>
    //           </div>
    //         );
    //       } else if (this.props.dishes.errMess) {
    //         return (
    //           <div className="container">
    //             <div className="row">
    //               <div className="col-12">
    //                 <h4>{props.dishes.errMess}</h4>
    //               </div>
    //             </div>
    //           </div>
    //         );
    //       } else      
    //     return (
    //       <div className="container">
    //         <div className="row">                
    //           <Media list>
    //               {menu}
    //           </Media>
    //         </div>
    //       </div>
    //     );
    // }
    render() {
        // const { data } = this.state;
        const HomePage = () => {
            return(
                <Home 
                />
            );
          }

        const BlogPage = () => {
            return (
                <BlogList blogs={this.state.data}
                />
            );
        }

        const BlogDetailPage = ({ match }) => {
            // const z = parseInt(match.params.blogId, 10);
            // console.log(z);
            return (

                <BlogDetail blog={this.state.data.filter(
                    blog => blog.id === parseInt(match.params.blogId, 10)
                    )[0]
                } 
                />


            );


        }
        return (
            <div>

                <Switch>

                    <Route exact path='/' component={BlogPage} />
                    <Route exact path='/blog/:blogId' component={BlogDetailPage} />
                    <Route exact path='/home' component={HomePage} />

                </Switch>

            </div>

        );
    }    
}

export default withRouter(
    connect(
      mapStateToProps,
      mapDispatchToProps
    )(Main)
  );
