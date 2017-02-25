/**
 * @export
 * @class Review
 */
export default class Review {
  constructor(AppConstants, $http) {
    'ngInject';

    this._AppConstants = AppConstants;
    this._$http = $http;
  }
}
