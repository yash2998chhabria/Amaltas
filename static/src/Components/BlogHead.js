import React, { Component } from 'react';
import { Media } from 'reactstrap';
import RenderContent from './BlogContent'

class Blog extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedBlog: null,
            blogC: [
                {
                    "id": 1,
                    "title": "cncn",
                    "content": "<p>snc ns fnnnndndndd<em>ddddjndvndkdvllsv</em></p>"
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
                }
            ]
        }
    }
    GotToblo(blo) {
        console.log("hello", blo.id);
        this.setState({
            selectedBlog: blo
        })
    }

    render() {
        const mystyle = {
            display: "flex",
            flex: "1 1 auto"
        }
        const blog = this.state.blogC.map((blo) => {
            return (

                <div key={blo.id} class="col-12 mt-3">
                    <div className="card" onClick={() => this.GotToblo(blo)}>
                        <div className="card-horizontal" style={mystyle}>
                            <div className="img-square-wrapper">
                                <img className="" src="http://via.placeholder.com/300x180" alt="Card image cap">
                                </img>
                            </div>
                            <div className="card-body">
                                <h4 className="card-title">{blo.title}</h4>
                                <p className="card-text">{blo.content}</p>
                            </div>
                        </div>
                        <div className="card-footer">
                            <small className="text-muted">Last updated 3 mins ago</small>
                        </div>
                    </div>
                </div>


            );
        });
        return (
            <div className="container-fluid">
                <div className="row">

                    {blog}
                    <RenderContent blogC={this.state.selectedBlog}></RenderContent>
                </div>
            </div>
        );
    }


}
export default Blog; 