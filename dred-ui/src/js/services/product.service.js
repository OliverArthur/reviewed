/**
 * @export
 * @class Review
 */
export default class Reviews {
  constructor(AppConstants, $http, $q) {
    'ngInject';

    this._AppConstants = AppConstants;
    this._$http = $http;
    this._$q = $q;
  }

  get(product) {
    let request = {};
  }
}
