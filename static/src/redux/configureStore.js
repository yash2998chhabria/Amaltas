import {createStore, combineReducers} from 'redux';
import { Dishes } from './dishes';

export const ConfigureStore = () => {
    const store = createStore(
        combineReducers({
            dishes: Dishes
        })
    );

    return store;
}