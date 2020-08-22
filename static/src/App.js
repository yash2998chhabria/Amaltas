import React, { Component } from 'react';
import Main from './Components/MainComponent'
import { Provider } from 'react-redux';
import { ConfigureStore } from './redux/configureStore';


const store = ConfigureStore();

class App extends Component {
    render(){
        return(
            <Provider store={store}>
            <div>
            <h1>This is JSX. LETS FUCK SHIT UP</h1>
            <Main />
            </div>
            </Provider>
        );
    }    
}

export default App;