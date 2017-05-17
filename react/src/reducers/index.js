import {combineReducers} from 'redux';
import flag from "./flag";
import solution from "./solution";
import {routerReducer} from 'react-router-redux';

export default combineReducers({
	router: routerReducer,
	flag,
	solution
})
