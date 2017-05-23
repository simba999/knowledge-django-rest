import React, {
  Component,
  PropTypes
}                       			from 'react';
import {connect} 					from 'react-redux';
import {
	getSolutionParentId, 
	fetchSolution,
	getCategoryName
} 									from '../../actions/solution';
import Modal						from 'react-bootstrap-modal';

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
    getCategoryName: () => dispatch(getCategoryName()),
    fetchSolution: () => dispatch(fetchSolution())
  };
}

class ResultDetailComponent extends React.Component {
	constructor(props, context) {
		super(props, context);

		this.state = {
			parentId: 0,
			solutions: [],
			solutionLists: 0,
			openModal: false,
			closeModal: false
		}
		console.log("Contstructor", this.props.location.pathname);
	}

	componentWillMount() {
		const { fetchSolution, getCategoryName } = this.props;

		this.setState({ parentId: this.props.location.pathname.split("/").splice(-1)[0] });
		fetchSolution();
		// getCategoryName();
	}

	solutionDetail(id) {
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
		console.log("nextProps: ", nextProps.data);
		console.log("prevProps: ", prevProps.data);

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
		let categoryIdList = [];
		let categoryName = '';
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
		console.log("categoryList: ", categoryList);
		this.setState({solutionByCategory: categoryList});
	}

	customSolution(id) {
		console.log("Id: ", id);
		window.location = '/solution-detail/' + id
		if (typeof id == 'undefined') {
			window.location = '/solution-detail'
		}
	}

	openModal() {
		this.setState({openModal: true});
	}

	closeModal()
	 {
	 	this.setState({openModal: false});
	 }
	render() {
		return (
			<div className="section">
				<div className="section__header section__header--thin no-border">
					<div className="section-header">
						<div className="section-header__item">
							<div className="section__back">
								<a className="btn-circle btn-circle--back" href="/"></a>
							</div>
						</div>
						<div className="section-header__item section-header__item--forced-center">
							<div className="section-header-circle">Request</div>
						</div>
						<div className="section-header__item section-header__item--right">
							<div className="section__buton">
								<div className="btn" onClick={() => this.openModal()}>Selection Solution</div>
							</div>
						</div>
					</div>
				</div>
				<div className="section__body">
					<div className="section_description">
						<div className="section-description">
							<div className="section-description__title">
								Request #3 Type and Title
							</div>
							<div className="section-description__text">
								Requested Date: <span> 04/12/2017 </span>
							</div>
							<div className="section-description__separator separator"></div>
						</div>
					</div>
				</div>
				<Modal
			        show={this.state.openModal}
			        onHide={this.closeModal.bind(this)}
			        className="createSolutionDialog"
			        aria-labelledby="ModalHeader">
			        <Modal.Body>
			          <div className="header__text">
			          	<div className="header-text__close-button">
			            	<label className="btn-icon btn-icon--remove"></label>
			            </div>
			            <div className="header-text__title">Create a solution</div>
			          </div>
			          <div className="">
			            ABC
			          </div>
			        </Modal.Body>
			      </Modal>
			</div>

		);
	}
}

ResultDetailComponent.propTypes = {
	parentID: PropTypes.string.isRequired,
}

// export default CustomSolutionComponent;

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(ResultDetailComponent);
