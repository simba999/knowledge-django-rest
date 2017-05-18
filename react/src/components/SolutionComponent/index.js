import React, {
  Component,
  PropTypes
}                       							from 'react';
import {connect} 									from 'react-redux';
import {fetchSolution} 								from '../../actions/solution';
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
    fetchSolution: () => dispatch(fetchSolution()),
    fetchCategories: () => dispatch(fetchCategories()),
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
		const { fetchSolution, fetchCategories } = this.props;
		
		fetchSolution();
	}

	componentWillReceiveProps(nextProps, prevProps) {
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

		for (let item in solutionArr) {
			let tempArr = {};

			// check if the input item belongs to the exixting list.
			if ( categoryIdList.includes(solutionArr[item]['category']['id']) == false ) {
				tempArr['categoryId'] = solutionArr[item]['category']['id'];
				tempArr['count'] = 1;
				tempArr['categoryName'] = solutionArr[item]['category']['name'];
				tempArr['id'] = solutionArr[item]['id']

				if (solutionArr[item]['status'] == -1) {
					tempArr['request'] = 1;
				} 
				else {
					tempArr['request'] = 0;
				}

				categoryList.push(tempArr);
				categoryIdList.push(tempArr['categoryId'])
			}
			else {
				for (let list in categoryList ) {
					if (solutionArr[item]['category']['id'] == categoryList[list]['categoryId']) {
						categoryList[list]['categoryId'] = solutionArr[item]['category']['id'];
						categoryList[list]['count'] += 1;

						if (solutionArr[item]['status'] == -1) {
							categoryList[list]['request'] += 1;
						}
					}
				}
			}
		}

		this.setState({solutionByCategory: categoryList});
	}

	customSolution(event) {
		console.log("Event: ", event);
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