import React, {
  Component,
  PropTypes
}                       from 'react';
import {connect} 		from 'react-redux';
import {getSolutionParentId, fetchSolutionByParentId} from '../../actions/solution';

function mapStateToProps(state) {
	console.log("Parent State: ", state);
	return {
		parentId: state.solution.parentId,
		data: state.solution.data
	}
}

function mapDispatchToProps(dispatch) {
  return {
    getSolutionParentId: () => dispatch(getSolutionParentId()),
    fetchSolutionByParentId: (id) => dispatch(fetchSolutionByParentId(id))
  };
}

class CustomSolutionComponent extends React.Component {
	constructor(props, context) {
		super(props, context);

		this.state = {
			parentId: 0,
			solutions: [],
			solutionLists: 0
		}
		console.log("Contstructor", this.props.location.pathname);
	}

	componentWillMount() {
		const { fetchSolutionByParentId } = this.props;

		this.setState({ parentId: this.props.location.pathname.split("/").splice(-1)[0] });
		fetchSolutionByParentId(this.props.location.pathname.split("/").splice(-1)[0]);
	}

	solutionDetail() {
		console.log("Custom solution event call");
		window.location = '/solution-detail';
	}
	componentDidMount(nextProps, prevProps) {
		// let solutionData = this.props.data;
		// console.log("Solutions: ", this.props.data);
		// this.divideByCategory(solutionData);
	}

	componentWillReceiveProps(nextProps, prevProps) {
		let solutionData = prevProps;

		if (nextProps != prevProps && typeof nextProps.data != 'undefined') {
			solutionData = nextProps.data;
			// this.divideByCategory(solutionData);
			this.setState({solutions: nextProps.data});
		}
		else {
			// this.divideByCategory(this.state.solutions);
		}
		// console.log("Solutions: ", nextProps.data);
		// this.divideByCategory(solutionData);
	}

	divideByCategory(solutionArr) {
		let categoryList = [];
		let categoryIdList = []
		console.log("solutionArr: ", solutionArr);
		for (let item in solutionArr) {
			let tempArr = {};
			console.log("item: ", item);
			console.log("itemData: ", solutionArr[item]);

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
		console.log('CATE: ', categoryList)
		this.setState({solutionByCategory: categoryList});
	}

	customSolution(id) {
		console.log("Id: ", id);
		window.location = '/solution-detail'
		if (typeof id == 'undefined') {
			window.location = '/solution-detail'
		}
	}

	render() {
		return (
			<div className="section">
				<div className="section__header">
					<div className="section-header">
						<div className="section__title">
							<div className="section-title">
								CUSTOM PURCHASE
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
								{solution.status == -1 ?
									<div className="solution-library__request"> 
										<span id="request-number" > 1 </span> Requests 
									</div>
								:
									""
								}
								<div className="solution-library__title" sid={solution.id} onClick={(event) => this.customSolution(solution.id, this)}> <span> { solution['name'] } </span> </div>
								<div className="solution-library__count">
									<div>
										<span className="solution-library-count__number"> 1 </span> Solutions 
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

CustomSolutionComponent.propTypes = {
	parentID: PropTypes.string.isRequired,
}

// export default CustomSolutionComponent;

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(CustomSolutionComponent);
