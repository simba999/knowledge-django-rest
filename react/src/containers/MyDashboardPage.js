import React from 'react';
import {connect} from 'react-redux';


class MyDashboardPage extends React.PureComponent {
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
													<div className="table-col table-col--date">data uploaded</div>
													<div className="table-col table-col--label">data used</div>
													<div className="table-col table-col--label">used by</div>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
											<div className="table-group" onClick={(event) => this.gotoAlgorithmPage(this)}>
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
			</section>
		);
	}
}

export default connect()(MyDashboardPage);