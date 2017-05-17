import {FLAG_TOGGLE} from '../constants';
import {GET_SOLUTION_BUY_USER} from '../constants';
import solutionApi 					from '../api/solutionApi';

export function flagToggle() {
	return {
		type: FLAG_TOGGLE
	}
}

// export function getSolutionLibraryByUser(data) {
// 	// let solutions = await fetchSolution()
// 	// fetchSolution().then((json) => {
// 	// 	console.log('dsssssssssssssssssssssssssssss',json)
// 	// 	solutions = json
// 	// })	
// 	return {
// 		type: GET_SOLUTION_BUY_USER,
// 		data: data
// 	}
// }

// export function fetchSolution() {
// 	return (dispatch) => {

// 		return fetch('http://localhost:8000/solution')
// 			.then(response => response.json())
// 			.then(json => {
// 				console.log('dddddddddddddddddddddddddd', json)
// 				dispatch(getSolutionLibraryByUser(json))
// 			});
// 	  }
	
// }