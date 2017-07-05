var gulp = require('gulp');
const wbBuild = require('workbox-build');
var webpackStream = require('webpack-stream');
var webpack2 = require('webpack');

var build = ['build']

gulp.task('default',build,function(){});

gulp.task('build',function(){
    var config = require('./webpack.config.js');
    return gulp.src('src/entry.js')
        //.pipe(webpack( require('./webpack.config.js') ))
        .pipe(webpackStream(config, webpack2))
        .pipe(gulp.dest('src/dist/'));
});


gulp.task('watch', function() {
  gulp.watch(['src/*.js','src/components/*.js','src/utils/*.js'],build);
});

