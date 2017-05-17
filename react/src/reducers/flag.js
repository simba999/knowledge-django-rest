import {FLAG_TOGGLE, GET_SOLUTION_BUY_USER} from '../constants';
console.log("REduecer")
export default (state = {active: false, count: 0}, action) => {
	switch (action.type) {
		case FLAG_TOGGLE:
			return {active: !state.active, count: state.count + 1};
		case GET_SOLUTION_BUY_USER:
			console.log("By User: ", action)
			return {active: 1, data:action.data}
		default:
			return state;
	}
}

// export function getSolutionLibraryByUser() {
// 	console.log("Action: ")
// 	return {
// 		type: GET_SOLUTION_BUY_USER
// 	}
// }
