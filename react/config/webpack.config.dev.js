const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base');
const PORT = process.env.PORT || 8080;

const DEVELOPMENT = 'development';

const config = {
	entry: [
		'react-hot-loader/patch',
		`webpack-dev-server/client?http://localhost:${PORT}`,
		'webpack/hot/only-dev-server',
		'./index.js'
	],
	devtool: "source-map",
	devServer: {
		// proxy: {
		// 	"/api": {
		// 		target: `http://localhost:${PORT}`,
		// 		// pathRewrite: {"^/api": ""}
		// 	}
		// },
		port: PORT,
		contentBase: path.join(__dirname, '../../public'),
		historyApiFallback: true,
		hot: true,
		publicPath: "/"
	},
	module: {
		rules: [
			{
				test: /\.scss$/,
				include: path.resolve(__dirname, '../src/styles'),
				use: [
					{
						loader: 'style-loader',
					},
					{
						loader: 'css-loader',
						options: {
							// importLoaders: 1,
							sourceMap: true
						}
					},
					{
						loader: "sass-loader"
					},
					{
						loader: 'postcss-loader'
					}
				]
			}
		]
	},
	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		// enable HMR globally

		new webpack.NamedModulesPlugin(),
		// prints more readable module names in the browser console on HMR updates

		new webpack.DefinePlugin({
			'process.env.NODE_ENV': JSON.stringify(DEVELOPMENT)
		})
	],
};

module.exports = merge(baseConfig, config);
