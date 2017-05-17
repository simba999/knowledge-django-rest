import React, {
  Component,
  PropTypes
}                       							from 'react';
import {connect} 									from 'react-redux';
import {fetchSolution, fetchCategories} 	from '../../actions/solution';
import solutionApi 									from '../../api/solutionApi';

function mapStateToProps(state) {
	console.log(state);
	return {
		data: state.solution.data
	}
}

function mapDispatchToProps(dispatch) {
  return {
    fetchSolution: () => dispatch(fetchSolution()),
    fetchCategories: () => dispatch(fetchCategories()),
  };
}


class SolutionComponent extends React.Component {
	constructor(props, context) {
		super(props, context);

		this.state = {
			solutions: []
		}
	}

	componentWillMount() {
		this.props.fetchSolution();
		this.props.fetchCategories();
	}

	componentWillReceiveProps(props) {
		this.setState({solutions: props.data});
	}

	divideByCategory(arr) {
		let categoryList = []

		for (let item in arr) {
			if ( categoryList.includes(item['category']) == false) {
				let tempArr = {};

				tempArr['category'] = item['category'];
				tempArr['count'] = 1;
				// tempArr['']
			}
		}
	}

	customSolution() {
		window.location = '/custom-solution';
	}

	render() {
		return (
			<div className="section">
				<div className="section__header">
					<div className="section-header">
						<div className="section__title">
							<div className="section-title">
								Solutions Library
							</div>
						</div>
						<div className="section__filter">
							<div className="filter">
								Filter by: Most Recent
							</div>
						</div>
						<div className="section__button">
							<div className="btn">
								+ Custom Solutions
							</div>
						</div>
					</div>
				</div>
				<div className="section__body">
					<div className="grid">
						{this.state.solutions.map((solution) => 
							<div className="solution-library">
								<div className="solution-library__request"> 
									<span id="request-number" > 03 </span> Requests 
								</div>
								<div className="solution-library__title" onClick={this.customSolution.bind(this)}> <span> { solution.name } </span> </div>
								<div className="solution-library__count">
									<div>
										<span className="solution-library-count__number"> 12 </span> Solutions 
									</div>
								</div>
							</div>
						)}
					</div>
				</div>
			</div>
		);
	}
}

SolutionComponent.propTypes = {
	data: PropTypes.object
}

// export default SolutionComponent;

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SolutionComponent);