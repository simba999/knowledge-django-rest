import React from 'react';
import {connect} from 'react-redux';


class SettingsPage extends React.PureComponent {
	render() {
		return (
			<h1>Settings</h1>
		);
	}
}

export default connect()(SettingsPage);
