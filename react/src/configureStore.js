import {createStore, applyMiddleware, compose} from 'redux';
import reducers from './reducers/index';
import thunk from 'redux-thunk';
import {routerMiddleware} from 'react-router-redux';
import history from './history';

// const middleware = routerMiddleware(history);
// const middleware = [routerMiddleware(history), thunk];

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ && process.env.NODE_ENV === 'development' ?
	window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ : compose;

export default function configureStore(initialState) {
	const store = createStore(reducers, initialState, composeEnhancers(
		applyMiddleware(thunk)
	));

	if (module.hot && process.env.NODE_ENV === 'development') {
		// Enable Webpack hot module replacement for reducers
		module.hot.accept('./reducers/index', () => {
			const nextRootReducer = require('./reducers/index').default;
			store.replaceReducer(nextRootReducer);
		});
	}

	return store;
}
