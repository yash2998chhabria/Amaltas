import {createStore, combineReducers, applyMiddleware } from 'redux';
import { Dishes } from './dishes';
import thunk from 'redux-thunk';
import logger from 'redux-logger';

export const ConfigureStore = () => {
    const store = createStore(
        combineReducers({
            dishes: Dishes
        }),
        applyMiddleware(thunk, logger)
    );

    return store;
}