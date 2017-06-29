const webpack = require('webpack');
const path = require('path');

const ENV = process.env.NODE_ENV || 'development';

module.exports = {
  entry:  './src/index.js',
  output: {
    path: `./src/dist/`,
    publicPath: __dirname,
    filename: 'bundle.js',
  },

  resolve: {
    extensions: ['','.jsx', '.js'],
  },

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: './node_modules/',
        loader: 'babel-loader',
      },
    ],
  },

  plugins: ENV === 'production' ? [
    new webpack.optimize.UglifyJsPlugin({
      minimize: true,
      compress: { warnings: false },
    }),
  ] : [],

  stats: {
    colors: true,
  },
  
  devServer: {
    disableHostCheck: true,
  },
};