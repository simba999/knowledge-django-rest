import React, {
  Component,
  PropTypes
}                       from 'react';
import {Link} 			from 'react-router-dom';
import {connect} 		from 'react-redux';

import {
  	fetchSolution, 
  	setSolutionParentId,
  	setSolutionData,
  	setCategoryName
} 													from '../../actions/solution';
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
    fetchSolution: (id) => dispatch(fetchSolution()),
    setCategoryName: (categoryName) => dispatch(setCategoryName(categoryName)),
    fetchCategories: () => dispatch(fetchCategories()),
    setSolutionParentId: () => dispatch(setSolutionParentId()),
    setSolutionData: (data) => dispatch(setSolutionData(data))
  };
}

class SubSolutionComponent extends React.Component {
	constructor(props, context) {
		super(props, context);
	}

	componentWillMount() {
		const { fetchSolution } = this.props;
		this.setState({ parentId: this.props.location.pathname.split("/").splice(-1)[0] });
		fetchSolution();
	}

	componentWillReceiveProps(nextProps, prevProps) {
		console.log("nextProps: ", nextProps);
		console.log("prevProps: ", prevProps);
		let solutionData = prevProps;

		if (nextProps != prevProps && typeof nextProps.data != 'undefined') {
			solutionData = nextProps.data;
			this.setState({solutions: nextProps.data});
		} 
		
		this.divideByCategory(solutionData, this.state.parentId);
	}

	divideByCategory(solutionArr, categoryID) {
		let categoryList = [];
		let categoryIdList = []
		console.log("solutionArr: ", solutionArr);
		console.log("categoryID: ", categoryID);
		for (let item in solutionArr) {
			let tempArr = {};
			console.log("itemArr: ", solutionArr[item]['category']);
			// check if the input item belongs to the exixting list.
			if (solutionArr[item]['category']['id'] == categoryID) {
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
		}
		console.log("Total: ", categoryList);
		this.setState({solutionByCategory: categoryList});
	}

	gotoAlgorithmPage() {
		this.context.router.history.push("/algorithm-detail");
	}


	render() {
		return (
			<div className="section">
				<div className="section__header">
					<div className="section-header">
						<div className="section__title">
							<div className="section-title">
								$SOLUTION_NAME$
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
					<div className="section-columns">
						<div className="section-column section-column-left">
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	<div className="sidebar__item">
				          		<div className="sidebar-rect">
				          			<span> NO PURCHASE IN PRODUCT </span>
				          		</div>
				          	</div>
				          	
					    </div>
					
						<div className="section-column section-column-right">
							<div className="section-column__header">
								<div className="section-column-header">
									Requests for Soltutions (RFS)
								</div>
								<div className="section-column-header-dec">
									Here represented all the request for the NO PURCHASE IN TARGETED MONTH solution
								</div>
								<div className="separator">
									<div className="btn-label separator-content">
										<span className="orange-color"> 8 </span>
										Alogorithms/Models
									</div>
								</div>
							</div>
							<div className="section-column__body">
								<div className="table">
									<div>
									<div className="table__header">
										<div className="table__row">
											<div className="table-row table-row--fluid">
												<div className="table-col table-col--label"></div>
												<div className="table-col table-col--name">Name</div>
												<div className="table-col table-col--date">Last Run</div>
												<div className="table-col table-col--label">score</div>
												<div className="table-col table-col--label"></div>
											</div>
											<div className="table-row">
												<div className="table-col table-col--label"></div>
											</div>
										</div>
									</div>
									</div>
									<div className="table__body">
										<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
											<div className="table-row table-row--fluid">
												<div className="table-col table-col--label"></div>
												<div className="table-col table-col--name">Request #1 type and Title</div>
												<div className="table-col table-col--date">01-12-2017</div>
												<div className="table-col table-col--score">
													<div className="table-col-score--increase">243</div>
												</div>
												<div className="table-col table-col--label">
													<div className="table-col-view">view</div>
												</div>
											</div>
											<div className="table-row">
												<div className="table-col table-col--compare">
													<div className="table-col-checkbox"></div>
												</div>
											</div>
										</div>
										<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
											<div className="table-row table-row--fluid">
												<div className="table-col table-col--label"></div>
												<div className="table-col table-col--name">Request #1 type and Title</div>
												<div className="table-col table-col--date">01-12-2017</div>
												<div className="table-col table-col--score">
													<div className="table-col-score--warning">243</div>
												</div>
												<div className="table-col table-col--label">
													<div className="table-col-view">view</div>
												</div>
											</div>
											<div className="table-row">
												<div className="table-col table-col--compare">
													<div className="table-col-checkbox"></div>
												</div>
											</div>
										</div>
										<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
											<div className="table-row table-row--fluid">
												<div className="table-col table-col--label"></div>
												<div className="table-col table-col--name">Request #1 type and Title</div>
												<div className="table-col table-col--date">01-12-2017</div>
												<div className="table-col table-col--score">
													<div className="table-col-score--stable">243</div>
												</div>
												<div className="table-col table-col--label">
													<div className="table-col-view">view</div>
												</div>
											</div>
											<div className="table-row">
												<div className="table-col table-col--compare">
													<div className="table-col-checkbox"></div>
												</div>
											</div>
										</div>
										<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
											<div className="table-row table-row--fluid">
												<div className="table-col table-col--label"></div>
												<div className="table-col table-col--name">Request #1 type and Title</div>
												<div className="table-col table-col--date">01-12-2017</div>
												<div className="table-col table-col--score">
													<div className="table-col-score--decrease">243</div>
												</div>
												<div className="table-col table-col--label">
													<div className="table-col-view">view</div>
												</div>
											</div>
											<div className="table-row">
												<div className="table-col table-col--compare">
													<div className="table-col-checkbox"></div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

// export default SubSolutionComponent;
SubSolutionComponent.propTypes = {
	parentID: PropTypes.string.isRequired,
}

SubSolutionComponent.contextTypes = {
  router: React.PropTypes.object
};

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SubSolutionComponent);