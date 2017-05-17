const PRODUCTION = 'production';

const NODE_ENV = process.env.NODE_ENV;
const isProduction = NODE_ENV === PRODUCTION;

module.exports = () => {
	if (isProduction) {
		return require('./config/webpack.config.prod');
	}

	return require('./config/webpack.config.dev');
};
