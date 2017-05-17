import React, {
  Component,
  PropTypes
}                       from 'react';
import {connect} 		from 'react-redux';
import {getSolutionLibraryByUser} from '../../actions/flag';

function mapStateToProps(state) {
	return {}
}

function mapDispatchToProps(dispatch) {
  return {
    getSolutionLibraryByUser: () => dispatch(getSolutionLibraryByUser()),
  };
}

class SolutionComponent extends React.Component {
	constructor(props, context) {
		super(props, context);
	}

	componentDidMount() {
		const { getSolutionLibraryByUser } = this.props;
		let result = getSolutionLibraryByUser();
		console.log('Result: ', result);
	}

	customSolution() {
		console.log("Custom solution event call");
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
						<div className="solution-library">
							<div className="solution-library__request"> 
								<span id="request-number" > 03 </span> Requests 
							</div>
							<div className="solution-library__title" onClick={this.customSolution.bind(this)}> <span> PRODUCT PURCHASE </span> </div>
							<div className="solution-library__count">
								<div>
									<span className="solution-library-count__number"> 12 </span> Solutions 
								</div>
							</div>
						</div>
						<div className="solution-library">
							<div className="solution-library__request"> 
								<span id="request-number" > 03 </span> Requests 
							</div>
							<div className="solution-library__title" onClick={this.customSolution.bind(this)}> <span> PRODUCT PURCHASE </span> </div>
							<div className="solution-library__count"> 
								<div>
									<span className="solution-library-count__number"> 12 </span> Solutions 
								</div>
							</div>
						</div>
						<div className="solution-library">
							<div className="solution-library__title"> <span> PRODUCT PURCHASE </span> </div>
							<div className="solution-library__count"> 
								<div>
									<span className="solution-library-count__number"> 12 </span> Solutions 
								</div>
							</div>
						</div>
						<div className="solution-library">
							<div className="solution-library__title"> <span> PRODUCT PURCHASE </span> </div>
							<div className="solution-library__count"> Solutions </div>
						</div>
						<div className="solution-library">
							<div className="solution-library__request"> 
								<span id="request-number" > 03 </span> Requests 
							</div>
							<div className="solution-library__title"> <span> PRODUCT PURCHASE </span> </div>
							<div className="solution-library__count"> Solutions </div>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

SolutionComponent.propTypes = {
	getSolutionLibraryByUser: PropTypes.func.isRequired,
}

// export default SolutionComponent;

export default connect(
	mapStateToProps,
  	mapDispatchToProps
)(SolutionComponent);