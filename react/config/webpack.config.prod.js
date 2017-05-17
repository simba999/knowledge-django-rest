const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const PRODUCTION = 'production';

const extractCss = new ExtractTextPlugin("styles.css");

const config = {
	entry: [
		'./index.js'
	],
	output: {
		filename: "bundle.js",
		path: path.resolve(__dirname, '../../public'),
		publicPath: "/"
	},
	devtool: false,
	module: {
		rules: [
			{
				test: /\.scss$/,
				include: path.resolve(__dirname, '../src/styles'),
				use: extractCss.extract([
					{
						loader: 'css-loader',
						options: {
							// importLoaders: 1,
							minimize: true,
						}
					},
					{
						loader: "sass-loader"
					},
					{
						loader: 'postcss-loader'
					}
				]),
			}
		]
	},
	plugins: [
		new webpack.DefinePlugin({
			'process.env.NODE_ENV': JSON.stringify(PRODUCTION)
		}),
		new webpack.optimize.UglifyJsPlugin(),
		extractCss,
	],
};

module.exports = merge(baseConfig, config);
