var gulp = require('gulp');
const wbBuild = require('workbox-build');
var webpack=require('gulp-webpack');
var sass = require('gulp-sass');

var build = ['build']

gulp.task('default',build,function(){});

gulp.task('sass', function () {
  return gulp.src('src/css/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('src/css'));
});

gulp.task('build',['sass'],function(){
    return gulp.src('src/entry.js')
        .pipe(webpack( require('./webpack.config.js') ))
        .pipe(gulp.dest('src/dist/'));
});
