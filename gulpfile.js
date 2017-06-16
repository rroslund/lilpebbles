var gulp = require('gulp');
const wbBuild = require('workbox-build');

gulp.task('bundle-sw', () => {
	return wbBuild.generateSW({
		globDirectory: './src/',
		swDest: './src/sw.js',
		staticFileGlobs: ['**\/*.{html,js,css}'],
														globIgnores: ['admin.html'],
														templatedUrls: {
														'/shell': ['shell.hbs', 'main.css', 'shell.css'],
														},
														})
														.then(() => {
														console.log('Service worker generated.');
														})
														.catch((err) => {
														console.log('[ERROR] This happened: ' + err);
														});
														})
