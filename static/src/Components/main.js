import React , { Component } from 'react'
import Axios from 'axios'
import BlogList from './list'
import BlogDetail from './detail'
import { Switch, Route } from 'react-router-dom';


class Mainfake extends Component {

    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            data: [{
                "id": 1,
                "blogId": 1,
                "title": "cncn",
                "content": "<p>snc ns fnnnnd ndndd< em>ddd djndvndk dvllsv</em></p>"
            },
            {
                "id": 2,
                "blogId": 2,
                "title": "hsvhufshufuz",
                "content": "snvjsnjs"
            },
            {
                "id": 3,
                "blogId": 3,
                "title": "hsvhufshufuz",
                "content": "snvjsnjs"
            }],
            error: null,
            blog: [],
            blogid: null
        }

    }


    render() {
        const { data } = this.state;
        const BlogPage = () => {
            return (
                <BlogList blogs={data}
                />
            );
        }

        const BlogDetailPage = ({ match }) => {
            const z = parseInt(match.params.blogId, 10);
            console.log(z);
            return (

                <BlogDetail blog={this.state.data.filter((data) => data.id === parseInt(match.params.blogId, 10))[0]} />


            );


        }
        return (
            <div>

                <Switch>

                    <Route path='/blog' component={BlogPage} />
                    <Route exact path='/blog/:blogId' component={BlogDetailPage} />

                </Switch>

            </div>

        );
    }
}

export default Mainfake;
