import angular from 'angular';

let directivesModule = angular.module('app.directives', []);

import RatingsStartDirective from './ratings-start/ratings-start.directive'
directivesModule.directive('ratingsStart', () => new RatingsStartDirective);

export default directivesModule;
