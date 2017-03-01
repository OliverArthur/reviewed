const gulp = require('gulp');
const notify = require('gulp-notify');
const source = require('vinyl-source-stream');
const browserify = require('browserify');
const babelify = require('babelify');
const ngAnnotate = require('browserify-ngannotate');
const browserSync = require('browser-sync').create();
const rename = require('gulp-rename');
const templateCache = require('gulp-angular-templatecache');
const uglify = require('gulp-uglify');
const merge = require('merge-stream');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
// Where our files are located
const jsFiles = "src/js/**/*.js";
const viewFiles = "src/js/**/*.html";

const interceptErrors = function (error) {
  const args = Array.prototype.slice.call(arguments);

  // Send error to notification center with gulp-notify
  notify.onError({
    title: 'Compile Error',
    message: '<%= error.message %>'
  }).apply(this, args);

  // Keep gulp from hanging on this task
  this.emit('end');
};


gulp.task('browserify', ['views'], () => browserify('./src/js/app.js')
  .transform(babelify, {
    presets: ["es2015"]
  })
  .transform(ngAnnotate)
  .bundle()
  .on('error', interceptErrors)
  //Pass desired output filename to vinyl-source-stream
  .pipe(source('main.js'))
  // Start piping stream to tasks!
  .pipe(gulp.dest('./build/')));

gulp.task('html', () => gulp.src("src/index.html")
  .on('error', interceptErrors)
  .pipe(gulp.dest('./build/')));

gulp.task('css', () => {
  return gulp.src('./src/main.scss')
    .pipe(sass())
    .pipe(gulp.dest('./build/'));
});

gulp.task('views', () => gulp.src(viewFiles)
  .pipe(templateCache({
    standalone: true
  }))
  .on('error', interceptErrors)
  .pipe(rename("app.templates.js"))
  .pipe(gulp.dest('./src/js/config/')));

// This task is used for building production ready
// minified JS/CSS files into the dist/ folder
gulp.task('build', ['html', 'css', 'browserify'], () => {
  const html = gulp.src("build/index.html")
    .pipe(gulp.dest('./dist/'));

  const css = gulp.src("build/main.css")
    .pipe(uglify())
    .pipe(gulp.dest('./dist/'));

  const js = gulp.src("build/main.js")
    .pipe(sourcemaps.init())
    .pipe(uglify())
    .pipe(sourcemaps.write('maps'))
    .pipe(gulp.dest('./dist/'));

  return merge(html, css, js);
});

gulp.task('default', ['html', 'css', 'browserify'], () => {

  browserSync.init(['./build/**/**.**'], {
    open: 'external',
    server: "./build",
    host: '0.0.0.0',
    port: 3000,
    notify: false,
    ui: {
      port: 4001
    }
  });

  gulp.watch("./src/index.html", ['html']);
  gulp.watch(viewFiles, ['views']);
  gulp.watch(jsFiles, ['browserify']);
  gulp.watch("./src/js/**/*.scss", ['css']);
});
