function ReviewsConfig($stateProvider) {
  'ngInject';

  $stateProvider
    .state('app.reviews', {
      url: '/',
      controller: 'ReviewsCtrl',
      controllerAs: '$ctrl',
      templateUrl: 'reviews/reviews.html',
      title: 'Reviews'
    });

};

export default ReviewsConfig;
