import {FLAG_TOGGLE} from '../constants';
console.log("REduecer")
export default (state = {active: false, count: 0}, action) => {
	switch (action.type) {
		case FLAG_TOGGLE:
			return {active: !state.active, count: state.count + 1};
		default:
			return state;
	}
}

