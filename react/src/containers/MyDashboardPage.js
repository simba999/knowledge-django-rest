import React from 'react';
import {connect} from 'react-redux';


class MyDashboardPage extends React.PureComponent {
	render() {
		return (
			<h1>My dashboard page</h1>
		);
	}
}

export default connect()(MyDashboardPage);