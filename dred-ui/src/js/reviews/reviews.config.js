function ReviewsConfig($stateProvider) {
  'ngInject';

  $stateProvider
    .state('app.reviews', {
      url: '/review?productName?productType',
      controller: 'ReviewsCtrl',
      controllerAs: '$ctrl',
      params: {
        productName: null,
        productType: null
      },
      templateUrl: 'reviews/reviews.html',
      title: 'Reviews'
    });

};

export default ReviewsConfig;
