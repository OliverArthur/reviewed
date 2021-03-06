/**
 * @param {any} $stateProvider 
 * @param {any} $locationProvider 
 * @param {any} $urlRouterProvider 
 */
function AppConfig($stateProvider, $locationProvider, $urlRouterProvider) {
  'ngInject';

  $locationProvider.html5Mode(true);

  $stateProvider
    .state('app', {
      abstract: true,
      templateUrl: 'layout/app-view.html'
    });

  $urlRouterProvider.otherwise('/');

}

export default AppConfig;
