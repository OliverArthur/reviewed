class ReviewsCtrl {
  constructor(Reviews, $state, $scope) {
    'ngInject';

    let reviews;

    this._Reviews = Reviews;
    this.reviews = reviews;
    this._$state = $state;
    this.isReadonly = false;
    this.changeOnHover = true;
    this.maxValue = 5;
    this.rating = 0;

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
