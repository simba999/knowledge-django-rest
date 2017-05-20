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

export function fetchSolution() {
	return (dispatch) => {
		return fetch('http://localhost:8000/solution')
			.then(response => response.json())
			.then(json => {
				dispatch(getSolutionLibraryByUser(json))
			});
	  }	
}

export function fetchSolutionHome(id) {
	console.log("AAa: ", typeof id)
	return (dispatch) => {
		return fetch('http://localhost:8000/users/' + id + '/home')
			.then(response => response.json())
			.then(json => {
				dispatch(getSolutionLibraryByUser(json))
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

export function fetchSolutionByParentId(id) {
	console.log("Here: ", typeof id);
	return (dispatch) => {
		return fetch('http://localhost:8000/solution/' + id + '/childsolution')
			.then(response => response.json())
			.then(json => {
				console.log("Result: ", json);
				dispatch(getSolutionByParentId(json))
			});
	  }	
}