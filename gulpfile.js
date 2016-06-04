var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', ['sass:watch']);

gulp.task('sass', function () {
  return gulp.src('./media/sass/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./media/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./media/sass/**/*.scss', ['sass', 'inject']);
});

gulp.task('inject', function(){
    var wiredep = require('wiredep').stream;
    var inject = require('gulp-inject');

    var injectSrc = gulp.src([
      './media/css/renda/*.css',
      './media/css/styles.css',
      './media/js/**/*.js'
    ], {read: false });

    var injectOptions = {
        ignorePath: '/media',
        addPrefix: '/static'
    };

    var options = {
      fileTypes: {
        html: {
          replace: {
            js: '<script src="/static{{filePath}}"></script>',
            css: '<link rel="stylesheet" href="/static{{filePath}}" />'
          }
        }
      },
      bowerJson: require('./bower.json'),
      directory: './media/lib',
      ignorePath: '../media'
    };

    return gulp.src('./templates/*.html')
        .pipe(wiredep(options))
        .pipe(inject(injectSrc, injectOptions))
        .pipe(gulp.dest('./templates'));

});
