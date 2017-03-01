/**
 * @export
 * @class Review
 */
export default class Products {
  constructor(AppConstants, $http, $q) {
    'ngInject';

    this._AppConstants = AppConstants;
    this._$http = $http;
    this._$q = $q;
  }

  getOneProduct(id) {
    let deferred = this._$q.defer();
    return this._$http({
      url: `${this._AppConstants.api}/v1/product/${id}`,
      method: 'GET',
    }).then(
      (res) => res.data,
      (err) => deferred.reject(err)
    );

  }
}
