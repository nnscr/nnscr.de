const gulp = require('gulp');
//const babel = require('gulp-babel');
const less = require('gulp-less');
//const connect = require('gulp-connect');
const del = require('del');
const exec = require("child_process").exec;

// source
/*var path_html  = [
    "src/main/app/*.html",
    "src/main/app/* /*.html",
    "src/main/app/* /* /*.html"
];
var path_js    = [
    "src/main/app/*.js",
    "src/main/app/* /*.js",
    "src/main/app/* /* /*.js"
];*/
var path_less  = "src/less/*.less";
var less_entry = "src/less/main.less";

// target
var path_dist_app = "nnscr/static/dist/app";
var path_dist_css = "nnscr/static/dist/css";

gulp.task('clean', function(cb) {
    del("nnscr/static/dist", cb);
});

gulp.task('es6', function() {
/*    return gulp.src(path_js)
        .pipe(babel({
            stage: 1,
            optional: [
                "es7.decorators"
            ]
        }))
        .pipe(gulp.dest(path_dist_app))
        .pipe(connect.reload());*/
});

gulp.task('less', function() {
 //   exec("yes yes | ./manage.py collectstatic -cl");
    return gulp.src(less_entry)
        .pipe(less())
        .pipe(gulp.dest(path_dist_css));
 //       .pipe(connect.reload());
});

gulp.task('watch', function() {
//    gulp.watch(path_js, ['es6']);
//    gulp.watch(path_html, ['html']);
    gulp.watch([path_less], ['less']);
});

/*gulp.task('html', () => {
    return gulp.src(path_html)
        .pipe(gulp.dest(path_dist_app))
        .pipe(connect.reload())
});*/

/*gulp.task('serve', () => {
    connect.server({
        root: 'public',
        livereload: true,
        fallback: 'public/index.html'
    })
});*/

gulp.task('app', ['es6']); // , 'html']);
gulp.task('build', ['app', 'less']);
gulp.task('default', ['build']);
