import React from 'react';
import render from './render';
import Root from './Root';

const rootNode = document.getElementById('root');

render(Root, rootNode);

// Hot Module Replacement API
if (module.hot && process.env.NODE_ENV === 'development') {
	module.hot.accept('./Root', () => {
		render(Root, rootNode);
	});
}
