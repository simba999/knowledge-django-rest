import React 						from 'react';
import {connect} 					from 'react-redux';
import Modal						from 'react-bootstrap-modal';


class MySolutionsPage extends React.PureComponent {
	constructor(props, context) {
		super(props, context);

		this.state = {
			openModal: false,
			closeModal: false
		}
		console.log("Contstructor", this.props.location.pathname);
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
			<section>
				<div className="section">
					<div className="section__header">
						<div className="section-header">
							<div className="section__title">
								<div className="section-title">
									Active Solutions
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
							<div className="section-column">
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
													<div className="table-col table-col--label">earned</div>
													<div className="table-col table-col--label"> in use</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--label"></div>
												</div>
											</div>
										</div>
										</div>
										<div className="table__body">
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--score">
														<div className="table-col-score--increase">243</div>
													</div>
													<div className="table-col table-col--label">147.34</div>
													<div className="table-col table-col--label">
														<div className="table-col-training" style={{'marginRight': '5px'}}>training</div>
														<div className="table-col-view">view</div>
													</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--score">
														<div className="table-col-score--warning">243</div>
													</div>
													<div className="table-col table-col--label">147.34</div>
													<div className="table-col table-col--label">
														<div className="table-col-training" style={{'marginRight': '5px'}}>training</div>
														<div className="table-col-view">view</div>
													</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--score">
														<div className="table-col-score--stable">243</div>
													</div>
													<div className="table-col table-col--label">147.34</div>
													<div className="table-col table-col--label">
														<div className="table-col-training" style={{'marginRight': '5px'}}>training</div>
														<div className="table-col-view">view</div>
													</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--score">
														<div className="table-col-score--decrease">243</div>
													</div>
													<div className="table-col table-col--label">147.34</div>
													<div className="table-col table-col--label">
														<div className="table-col-training" style={{'marginRight': '5px'}}>training</div>
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
				<div className="section">
					<div className="section__header">
						<div className="section-header">
							<div className="section__title">
								<div className="section-title">
									Data Sources
								</div>
							</div>
							<div className="section__filter">
								<div className="filter">
									Filter by: Most Recent
								</div>
							</div>
						</div>
					</div>
					<div className="section__body">
						<div className="section-columns">
							<div className="section-column">
								<div className="section-column__body">
									<div className="table">
										<div>
										<div className="table__header">
											<div className="table__row">
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Name</div>
													<div className="table-col table-col--label">actions</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--label"></div>
												</div>
											</div>
										</div>
										</div>
										<div className="table__body">
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--label">
														<div className="table-col-view">upload notebook</div>
													</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--label">
														<div className="table-col-view">upload notebook</div>
													</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--label">John doe</div>
													<div className="table-col table-col--label">147.34</div>
												</div>
												<div className="table-row">
													<div className="table-col table-col--compare">
														<div className="table-col-checkbox"></div>
													</div>
												</div>
											</div>
											<div className="table-group" onClick={(event) => this.openModal(this)}>
												<div className="table-row table-row--fluid">
													<div className="table-col table-col--label"></div>
													<div className="table-col table-col--name">Request #1 type and Title</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--date">01-12-2017</div>
													<div className="table-col table-col--label">John doe</div>
													<div className="table-col table-col--label">147.34</div>
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
				<Modal
			        show={this.state.openModal}
			        onHide={this.closeModal}
			        className="complete-detail-form"
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
				            <input type="text" placeholder="Enter the title of solution" />
				          </div>
				          <div className="content-text__item">
				            <input type="textarea" placeholder="Enter the description of solution" />
				          </div>
				          <div className="content-text__item">
				            <select>
				            	<option>Select a language</option>
				            </select>
				          </div>
				          <div className="content-text__item">
				            <input type="textarea" placeholder="Enter the details of the library associated with this algorithm" />
				          </div>
			          </div>
			          <div className="footer-text">
			          	<div className="btn-footer-text">Download Notebook</div>
			          </div>
			        </Modal.Body>
			      </Modal>
			</section>
		);
	}
}

export default connect()(MySolutionsPage);