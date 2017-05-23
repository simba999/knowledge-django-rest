import {
	GET_SOLUTION_BY_CATEGORY,
	GET_CATEGORIES,
	GET_SOLUTION_PARENT_ID,
	SET_SOLUTION_PARENT_ID,
	GET_SOLUTION_BY_PARENT_ID

} 									from '../constants';

import solutionApi 					from '../api/solutionApi';

export function getSolutionLibraryByUser(data) {
	return {
		type: GET_SOLUTION_BY_CATEGORY,
		data: data
	}
}

export function getSolutionByParentId(data) {
	return {
		type: GET_SOLUTION_BY_PARENT_ID,
		data: data
	}
}

export function getCategories(data) {
	return {
		type: GET_CATEGORIES,
		categories: data
	}
}

export function setSolutionParentId(id) {
	return {
		type: SET_SOLUTION_PARENT_ID,
		data: id
	}
}

export function getSolutionParentId() {
	return {
		type: GET_SOLUTION_PARENT_ID
	}
}

export function setUserID(id) {
	return {
		type: 'SET_USER_ID',
		userId: id
	}
}

export function setCategoryName(categoryName) {
	return {
		type: 'SET_CATEGORY_NAME',
		data: categoryName
	}
}
export function getCategoryName() {
	return {
		type: 'GET_CATEGORY_NAME'
	}
}

export function setSolutionData(data) {
	console.log("Solution Action", data);
	return {
		type: 'SET_SOLUTION_DATA',
		data: data
	}
}

export function fetchSolution() {
	return (dispatch) => {
		return fetch('http://localhost:8000/solution')
			.then(response => response.json())
			.then(json => {
				dispatch(getSolutionLibraryByUser(json))
				dispatch(setSolutionData(json));
			});
	  }	
}

export function fetchSolutionHome(id) {
	return (dispatch) => {
		return fetch('http://localhost:8000/users/' + id + '/home')
			.then(response => {
				return response.json();
			})
			.then(json => {
				console.log("AAa: ", json);
				dispatch(getSolutionLibraryByUser(json));
				dispatch(setUserID(id));
			});
	  }	
}

export function fetchCategories() {
	return (dispatch) => {
		return fetch('http://localhost:8000/categories')
			.then(response => response.json())
			.then(json => {
				dispatch(getCategories(json))
			});
	  }	
}

// export function fetchSolutionByCategoryId(id, token) {
// 	console.log("Here: ", id);
// 	token = "0a9e10c94172b7072944aa957cf8b909136a1d8f";
// 	return (dispatch) => {
// 		return fetch('http://localhost:8000/accounts/login', {
// 			method: 'POST',
// 			mode: 'cors',
// 			headers: new Headers({
// 				'Accept': 'application/json',
// 				'Access-Control-Allow-Origin':'*',
// 				'Content-Type': 'application/json'
// 			}),
// 			body: JSON.stringify({
// 				'username': 'admin',
// 				'password': 'simba126'
// 			})
// 		})
// 		.then(response => response.json())
// 		.then(json => {
// 			console.log("Result: ", json);
// 			dispatch(getSolutionByParentId(json));
// 			// dispatch(setUserID(id));
// 		});
// 	  }	
// }

// export function fetchSolutionByCategoryId22(id, token) {
// 	console.log("Here: ", id);
// 	token = "0a9e10c94172b7072944aa957cf8b909136a1d8f";
// 	return (dispatch) => {
// 		return fetch('http://localhost:8000/filter/solution', {
// 			method: 'POST',
// 			mode: 'cors',
// 			redirect: 'follow',
// 			headers: new Headers({
// 				'Accept': 'application/json',
// 				'Content-Type': 'application/json'
// 			}),
// 			body: JSON.stringify({
// 				filter: 'category_id',
// 				value: id,
// 				operator: '='
// 			})
// 		})
// 		.then(response => response.json())
// 		.then(json => {
// 			console.log("Result: ", json);
// 			dispatch(getSolutionByParentId(json));
// 			// dispatch(setUserID(id));
// 		});
// 	  }	
// }

export function fetchSolutionByCategoryId(id) {
	console.log("Here: ", typeof id);
	return (dispatch) => {
		return fetch('http://localhost:8000/categories/' + id + '/solutions')
			.then(response => response.json())
			.then(json => {
				console.log("Result: ", json);
				dispatch(getSolutionByParentId(json));
				// dispatch(setUserID(id));
			});
	  }	
}