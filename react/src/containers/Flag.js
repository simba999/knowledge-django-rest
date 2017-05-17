import React from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import {flagToggle} from '../actions';

class Flag extends React.PureComponent {
	constructor(props) {
		super(props);

		this.onClickHandler = this.onClickHandler.bind(this);
	}
	onClickHandler(e) {
		this.props.flagToggle();
	}
	render() {
		const {flag} = this.props;
		const message = flag.active ? 'Flag is active' : "Flag isn't active";

		return (
			<div>
				<button onClick={this.onClickHandler}>Toggle flag</button>
				{message}
				<p>Count: {flag.count}</p>
			</div>
		);
	}
}

Flag.propTypes = {
	flag: PropTypes.shape({
		active: PropTypes.bool.isRequired,
		count: PropTypes.number.isRequired
	}).isRequired,
	flagToggle: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
	flag: state.flag
});

const mapDispatchToProps = dispatch => ({
	flagToggle: () => dispatch(flagToggle())
});

export default connect(mapStateToProps, mapDispatchToProps)(Flag);
