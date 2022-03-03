const webpack = require('webpack');
const path = require("path");

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  optimization: {
    minimize: true,
},
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        //this affects react lib size
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
};