import ReviewService from './review.service'
import angular from 'angular';

// Create the module where our functionality can attach to
let servicesModule = angular.module('app.services', []);

servicesModule.service('Review', ReviewService);


export default servicesModule;
