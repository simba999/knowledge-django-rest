import {
	GET_SOLUTION_BY_CATEGORY,
	GET_CATEGORIES,
	GET_SOLUTION_PARENT_ID,
	SET_SOLUTION_PARENT_ID,
	GET_SOLUTION_BY_PARENT_ID
} from '../constants';

const initiateState = {
	active: 0,
	solutionParentId: 0,
	solutionChildId: 0,
	data: [],
	categories: [],
	parentId: 0
}

export default (state = initiateState, action) => {
	console.log("ReducerData: ", action)
	switch (action.type) {
		case GET_SOLUTION_BY_CATEGORY:
			return {
				...state,
				active: 1, 
				data: action.data
			}
		
		case GET_CATEGORIES:
			return {
				...state,
				active: 1,
				categories: action.categories
			}

		case SET_SOLUTION_PARENT_ID:
			return {
				...state,
				active: 1,
				parentId: action.data
			}
		case GET_SOLUTION_PARENT_ID:
			return {
				...state,
				active: 1,
			}

		case GET_SOLUTION_BY_PARENT_ID:
			return {
				...state,
				data: action.data
			}
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
