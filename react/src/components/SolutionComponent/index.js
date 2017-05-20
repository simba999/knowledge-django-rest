import React, {
  Component,
  PropTypes
}                       							from 'react';
import {connect} 									from 'react-redux';
import {fetchSolutionHome, setSolutionParentId} 								from '../../actions/solution';
import solutionApi 									from '../../api/solutionApi';

function mapStateToProps(state) {
	console.log("state: ", state);
	return {
		data: state.solution.data,
		categories: state.solution.categories
	}
}

function mapDispatchToProps(dispatch) {
  return {
    fetchSolutionHome: (id) => dispatch(fetchSolutionHome(id)),
    fetchCategories: () => dispatch(fetchCategories()),
    setSolutionParentId: () => dispatch(setSolutionParentId())
  };
}

class SolutionComponent extends React.Component {
	constructor(props, context) {
		super(props, context);

		this.state = {
			solutions: [],
			categories: [],
			solutionByCategory: []
		}

		this.divideByCategory = this.divideByCategory.bind(this);
		// this.customSolution = this.customSolution.bind(this);	
	}

	componentWillMount() {
		const { fetchSolutionHome, fetchCategories } = this.props;
		
		fetchSolutionHome(1);
	}

	componentWillReceiveProps(nextProps, prevProps) {
		console.log("nextProps: ", nextProps);
		console.log("prevProps: ", prevProps);
		let solutionData = prevProps;

		if (nextProps != prevProps && typeof nextProps.data != 'undefined') {
			solutionData = nextProps.data;
			this.setState({solutions: nextProps.data});
		} 
		
		this.divideByCategory(solutionData);
	}

	divideByCategory(solutionArr) {
		let categoryList = [];
		let categoryIdList = []
		console.log("solutionArr: ", solutionArr)
		for (let category in solutionArr) {
			console.log("parentCategory: ", category["Category"]);

			for (let parentCategory in category["Category"]) {

			}
			tempCategory = {}
			tempCategory['id'] = category['id']
			tempCategory['name'] = category['name']
			categoryList.push(tempCategory)
			// for (childCategory in category) {

			// }
		}

		this.setState({solutionByCategory: categoryList});
	}

	customSolution(id) {
		this.props.setSolutionParentId(id)
		window.location = '/custom-solution' + '/' + id;
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
						{this.state.solutionByCategory.map((solution) => 
							<div className="solution-library">
								{solution.request > 0 ?
									<div className="solution-library__request"> 
										<span id="request-number" > {solution.request} </span> Requests 
									</div>
								:
									""
								}
								<div className="solution-library__title" sid={solution.id} onClick={(event) => this.customSolution(solution.id, this)}> <span> { solution.categoryName } </span> </div>
								<div className="solution-library__count">
									<div>
										<span className="solution-library-count__number"> {solution.count} </span> Solutions 
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
	data: PropTypes.object,
	categories: PropTypes.object
}

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SolutionComponent);