class ReviewsCtrl {
  constructor(Reviews, Products, $stateParams, $state, $scope) {
    'ngInject';

    let reviews;
    this._Products = Products;
    this._Reviews = Reviews;
    this.reviews = reviews;
    this._$state = $state;
    this.isReadonly = false;
    this.changeOnHover = true;
    this.maxValue = 5;
    this.rating = 0;
    this.productType = $stateParams.productType;
    this.productName = $stateParams.productName;
    console.log(this.productType)
    console.log(this.productName)

    if (!(typeof (componentHandler) == 'undefined')) {
      componentHandler.upgradeAllRegistered();
    }

    this.reviews = {
      user_name: '',
      title: '',
      review: '',
      rating: 0,
      facebook: false,
      twitter: false,
      linkedin: false,
      published: true
    };
  }

  submit() {
    this.reviews.isSubmitting = true;
    this._Reviews.save(this.reviews).then(
      (res) => {
        this.reviews.success = res.message;
      },
      (err) => {
        this.reviews.isSubmitting = false;
        this.errors = err.data.errors;
      }
    )
  }
}

export default ReviewsCtrl;
