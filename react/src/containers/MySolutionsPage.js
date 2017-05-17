import React from 'react';
import {connect} from 'react-redux';


class MySolutionsPage extends React.PureComponent {
	render() {
		return (
			<h1>My solutions page</h1>
		);
	}
}

export default connect()(MySolutionsPage);