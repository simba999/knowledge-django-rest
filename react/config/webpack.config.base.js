const path = require('path');
const webpack = require('webpack');

module.exports = {
	context: path.resolve(__dirname, '../src'),
	target: "web",
	externals: {
		'react': 'React',
		'react-dom': 'ReactDOM'
	},
	module: {
		rules: [
			{
				test: /\.jsx?$/,
				include: path.resolve(__dirname, '../src'),
				loader: "babel-loader"
			},
		]
	},
};
