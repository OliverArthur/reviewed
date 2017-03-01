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

  save(payload) {
    let deferred = this._$q.defer();
    return this._$http({
      url: `${this._AppConstants.api}/v1/review`,
      method: 'POST',
      data: payload
    }).then(
      (res) => res.data,
      (err) => deferred.reject(err)
    );
  }
}
