import React, {
  Component,
  PropTypes
}                       from 'react';
import {Link} 			from 'react-router-dom';
import {connect} 		from 'react-redux';

class SolutionDetailComponent extends React.Component {
	constructor(props, context) {
		super(props, context);
	}

	componentDidMount() {
		// const { getSolutionLibraryByUser } = this.props;
		// getSolutionLibraryByUser();
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
					<div className="layout">
						<div className="layout__aside">
							<div className="sidebar">
						        <div className="sidebar__body">
						          	<div className="sidebar__item">
						          		<div className="sidebar-rect">
						          			<span> NO PURCHASE IN PRODUCT </span>
						          		</div>
						          	</div>
						          	<div className="sidebar__item">
						          		<div className="sidebar-rect">
						          			NO PURCHASE IN BRAND
						          		</div>
						          	</div>
						          	<div className="sidebar__item">
						          		<div className="sidebar-rect">
						          			NO PURCHASE IN IAMGE
						          		</div>
						          	</div>
						          	<div className="sidebar__item">
						          		<div className="sidebar-rect">
						          			NO PURCHASE IN PRODUCT
						          		</div>
						          	</div>

						        </div>
						    </div>
						</div>
						<div className="layout__main">
							<div className="layout__header">
								Requests for Soltutions (RFS)
								<br />
								Here represented all the request for the NO PURCHASE IN TARGETED MONTH solution
							</div>
							<div className="layout__content">

							</div>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default SolutionDetailComponent;