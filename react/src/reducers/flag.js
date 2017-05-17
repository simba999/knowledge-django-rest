import {FLAG_TOGGLE, GET_SOLUTION_BUY_USER} from '../constants';

export default (state = {active: false, count: 0}, action) => {
	switch (action.type) {
		case FLAG_TOGGLE:
			return {active: !state.active, count: state.count + 1};
		case GET_SOLUTION_BUY_USER:
			return {active: 1}
		default:
			return state;
	}
}
