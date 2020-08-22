import React, { Component } from 'react';
import { Media } from 'reactstrap';
//import axios from 'axios';
import { baseUrl } from '../shared/baseUrl';
import { connect } from 'react-redux';
import { fetchDishes } from '../redux/ActionCreators';
import { Loading } from './LoadingComponent';

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
            list : [],
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
        console.log(this.props);
        // fetch(baseUrl + 'api/article/')
        // .then(res => res.json())
        // .then((data) => {
        //   this.setState({ list : data })
        //   console.log(this.state.list)
        // })
        // .catch(console.log)
      }        
    

    render() {
        const menu = this.props.dishes.dishes.map((dish) => {
            return (
              <div key={dish.id} className="col-12 mt-5">
                <Media tag="li">
                  <Media left middle>
                      <Media object src={dish.image} alt={dish.name} />
                  </Media>
                  <Media body className="ml-5">
                    <Media heading>{dish.name}</Media>
                    <p>{dish.description}</p>
                  </Media>
                </Media>
              </div>
            );
        });

        // if (this.props.dishes.isLoading) {
        //     return (
        //       <div className="container">
        //         <div className="row">
        //           <Loading />
        //         </div>
        //       </div>
        //     );
        //   } else if (this.props.dishes.errMess) {
        //     return (
        //       <div className="container">
        //         <div className="row">
        //           <div className="col-12">
        //             <h4>{props.dishes.errMess}</h4>
        //           </div>
        //         </div>
        //       </div>
        //     );
        //   } else      
        return (
          <div className="container">
            <div className="row">                
              <Media list>
                  {menu}
              </Media>
            </div>
          </div>
        );
    }
}

export default   connect(
    mapStateToProps,
    mapDispatchToProps
  )(Main);