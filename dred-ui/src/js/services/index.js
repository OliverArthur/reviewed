import ReviewService from './review.service'
import angular from 'angular';

// Create the module where our functionality can attach to
let servicesModule = angular.module('app.services', []);

servicesModule.service('Reviews', ReviewService);


export default servicesModule;
