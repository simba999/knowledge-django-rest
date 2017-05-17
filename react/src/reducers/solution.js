import {
	GET_SOLUTION_BY_CATEGORY,
	GET_CATEGORIES
} from '../constants';

export default (state = {active: false, count: 0}, action) => {
	switch (action.type) {
		case GET_SOLUTION_BY_CATEGORY:
			return {active: 1, data:action.data}
		case GET_CATEGORIES:
			return {active: 1, data:action.categories}
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
