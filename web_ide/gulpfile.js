var gulp = require('gulp');
var Server = require('karma').Server;
var less = require('gulp-less');
var path = require('path');

var LessPluginCleanCSS = require('less-plugin-clean-css'),
    cleancss = new LessPluginCleanCSS({advanced: true});

gulp.task('less', function () {
    gulp.src('./web_ide/static/less/app.less') //path to your main less file
        .pipe(less({
            plugins: [cleancss]
        }))
        .pipe(gulp.dest('./web_ide/static/css')); // your output folder
});

gulp.task('test', function (done) {
    new Server({
        configFile: __dirname + '/karma.conf.js',
        singleRun: true
    }, done).start();
});