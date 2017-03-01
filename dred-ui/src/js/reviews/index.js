// Include our UI-Router config settings
import ReviewsConfig from './reviews.config';
// Controllers
import ReviewsCtrl from './reviews.controller';
import angular from 'angular';

// Create the module where our functionality can attach to
let reviewsModule = angular.module('app.reviews', []);

reviewsModule.config(ReviewsConfig);


reviewsModule.controller('ReviewsCtrl', ReviewsCtrl);


export default reviewsModule;
