import React, {
  Component,
  PropTypes
}                                 from 'react';
import {connect} from 'react-redux';
import {getSolutionLibraryByUser} from '../actions/flag';
import SolutionComponent from '../components/SolutionComponent';

function mapStateToProps(state) {
	return {}
}

function mapDispatchToProps(dispatch) {
  return {
    getSolutionLibraryByUser: () => dispatch(getSolutionLibraryByUser()),
  };
}

class SolutionLibraryPage extends React.Component {
	constructor(props, context) {
		super(props, context);
	}

	componentDidMount() {
		// const { getSolutionLibraryByUser } = this.props;
		// getSolutionLibraryByUser();
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
	getSolutionLibraryByUser: PropTypes.func.isRequired,
}

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SolutionLibraryPage);