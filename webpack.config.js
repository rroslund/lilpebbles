var path = require('path');

module.exports = {
  entry:{
      ordoesshe: './src/js/ordoesshe.js'
    },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, './src/dist')
  }
};