import React from 'react';
import {AppContainer} from "react-hot-loader";
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import configureStore from './configureStore';
import history from './history';
import {ConnectedRouter} from 'react-router-redux';

const PRELOADED_STATE = {};

const store = configureStore(PRELOADED_STATE);

let render;
if (process.env.NODE_ENV === 'development') {
	render = (Component, node) => {
		ReactDOM.render(
			<AppContainer>
				<Provider store={store}>
					<ConnectedRouter history={history}>
						<Component/>
					</ConnectedRouter>
				</Provider>
			</AppContainer>,
			node
		);
	};
} else {
	render = (Component, node) => {
		ReactDOM.render((
			<Provider store={store}>
				<ConnectedRouter history={history}>
					<Component/>
				</ConnectedRouter>
			</Provider>
		), node);
	}
}

export default render;

