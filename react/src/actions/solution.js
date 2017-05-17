import {GET_SOLUTION_BY_CATEGORY} 	from '../constants';
import {GET_CATEGORIES} 			from '../constants';
import solutionApi 					from '../api/solutionApi';

export function getSolutionLibraryByUser(data) {
	return {
		type: GET_SOLUTION_BY_CATEGORY,
		data: data
	}
}

export function getCategories(data) {
	return {
		type: GET_CATEGORIES,
		categories: data
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

export function fetchCategories() {
	return (dispatch) => {
		return fetch('http://localhost:8000/categories')
			.then(response => response.json())
			.then(json => {
				dispatch(getCategories(json))
			});
	  }
	
}