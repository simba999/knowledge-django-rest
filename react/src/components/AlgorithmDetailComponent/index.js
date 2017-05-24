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

class AlgorithmDetailComponent extends React.Component {
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
							<div className="section-header-circle">101.74</div>
						</div>
						<div className="section-header__item section-header__item--right">
							<div className="section__buton">
								<div className="btn" onClick={() => this.openModal()}>Improve Algorithm</div>
							</div>
						</div>
					</div>
				</div>
				<div className="section__body">
					<div className="section_description">
						<div className="section-description">
							<div className="section-description__title">
								Customers with more than 2 purchases (GMLER)
							</div>
							<div className="section-description__text">
								Last Run: <span> 04/12/2017 </span>
							</div>
							<div className="section-description__separator separator"></div>
						</div>
					</div>
					<div className="section__detail">
						<div className="section-detail__description">
							Sure, there are several way to recognize images and detect them by a number of features. But what i am worrying about is executive time to detect duplication among 600000. It take a lot of stuff.
							Sure, there are several way to recognize images and detect them by a number of features. But what i am worrying about is executive time to detect duplication among 600000. It take a lot of stuff.
							Sure, there are several way to recognize images and detect them by a number of features. But what i am worrying about is executive time to detect duplication among 600000. It take a lot of stuff.
							Sure, there are several way to recognize images and detect them by a number of features. But what i am worrying about is executive time to detect duplication among 600000. It take a lot of stuff.
							Sure, there are several way to recognize images and detect them by a number of features. But what i am worrying about is executive time to detect duplication among 600000. It take a lot of stuff.

						</div>
						<div className="section-detail__content">
							<div className="section-detail-content__item" id="caegory_info">
								<div className="content-item">
									<div className="content-item__title">Category</div>
									<div className="content-item__content uppercase">Category #3</div>
								</div>
							</div>
							<div className="section-detail-content__item">
								<div className="content-item">
									<div className="content-item__title">language</div>
									<div className="content-item__content uppercase">coming language</div>
								</div>
							</div>
							<div className="section-detail-content__item">
								<div className="content-item">
									<div className="content-item__title">library</div>
									<div className="content-item__content">details of library</div>
								</div>
							</div>
						</div>
					</div>
					<div className="section__title">
						<div className="uppercase">data components:</div>
					</div>
					<div className="section__additional">
						<div className="section-additional__column-left">
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
						</div>
						<div className="section-additional__column">
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
							<div className="section-additional-column__item">
								<span className="orange-color">&bull; </span>
								<span> Client's Customer Transaction Data </span>
								<span className="light-gray-color">propriety</span>
							</div>
						</div>
					</div>
				</div>
				<Modal
			        show={this.state.openModal}
			        onHide={this.closeModal}
			        className="createSolutionDialog"
			        aria-labelledby="ModalHeader">
			        <Modal.Body>
			          <div className="header-text">
			          	<div className="header-text__close-button">
			            	<label className="btn-icon btn-icon--remove" onClick={() => this.closeModal()}></label>
			            </div>
			            <div className="header-text__title">Create a solution</div>
			          </div>
			          <div className="content-text">
				          <div className="content-text__item">
				            <div className="content-text__title">Select language</div>
				            <div className="content-text__content">
				            	<div className="content-text-content__rect content-text-content__rect--selected">Python</div>
				            	<div className="content-text-content__rect">R</div>
				            	<div className="content-text-content__rect">Others</div>
				            </div>
				          </div>
				          <div className="content-text__item">
				            <div className="content-text__title">will you include custom data?</div>
				            <div className="content-text__content">
				            	<div className="content-text-content__rect content-text-content__rect--selected">Yes</div>
				            	<div className="content-text-content__rect">No</div>
				            </div>
				          </div>
			          </div>
			          <div className="footer-text">
			          	<div className="btn-footer-text">Download Notebook</div>
			          </div>
			        </Modal.Body>
			      </Modal>
			</div>

		);
	}
}

AlgorithmDetailComponent.propTypes = {
	parentID: PropTypes.string.isRequired,
}

// export default CustomSolutionComponent;

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(AlgorithmDetailComponent);
