import {FLAG_TOGGLE} from '../constants';
import {GET_SOLUTION_BUY_USER} from '../constants';

export function flagToggle() {
	return {
		type: FLAG_TOGGLE
	}
}

export function getSolutionLibraryByUser() {
	return {
		type: GET_SOLUTION_BUY_USER
	}
}