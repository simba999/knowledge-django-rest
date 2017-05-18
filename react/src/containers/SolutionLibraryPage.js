import React, {
  Component,
  PropTypes
}                                 from 'react';
import {connect} from 'react-redux';
import {fetchSolution, fetchCategories} 	from '../actions/solution';
import SolutionComponent from '../components/SolutionComponent';

function mapStateToProps(state) {
	// console.log("AA: ", state);
	return {
		data: state.solution.data,
		categories: state.solution.categories
	}
}

function mapDispatchToProps(dispatch) {
  return {
    fetchSolution: () => dispatch(fetchSolution()),
    fetchCategories: () => dispatch(fetchCategories()),
  };
}

class SolutionLibraryPage extends React.Component {
	constructor(props, context) {
		super(props, context);
	}

	componentDidMount() {
		// this.props.fetchSolution();
		// this.props.fetchCategories();
	}

	componentWillReceiveProps(props) {
		// this.setState({solutions: props.data});
		// this.setState({categories: props.categories});
		// this.state.solutions = props.data;
		// this.state.categories = props.categories;
		
	}

	solutionDetail() {
		console.log("Custom solution event call");
		window.location = '/my-dashboard';
		console.log("Custom solution event End call");
		// browserHistory.push('/my-dashboard');
	}

	render() {
		return (
			<SolutionComponent></SolutionComponent>
		);
	}
}

SolutionLibraryPage.propTypes = {
	data: PropTypes.object,
	categories: PropTypes.object,
	fetchSolution: PropTypes.func,
	fetchCategories: PropTypes.func
}

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SolutionLibraryPage);