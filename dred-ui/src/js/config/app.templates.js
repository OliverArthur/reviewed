angular.module('templates', []).run(['$templateCache', function($templateCache) {$templateCache.put('components/list-errors.html','<ul class="error-messages" ng-show="$ctrl.errors">\n  <div ng-repeat="(field, errors) in $ctrl.errors">\n    <li ng-repeat="error in errors">\n      {{field}} {{error}}\n    </li>\n  </div>\n</ul>\n');
$templateCache.put('layout/app-view.html','<app-header></app-header>\n\n<div ui-view class="dred-content__layout"></div>\n');
$templateCache.put('layout/footer.html','<footer class="mdl-mega-footer">\n\n  <div class="mdl-mega-footer__bottom-section">\n    <div class="mdl-logo">DrEd</div>\n    <ul class="mdl-mega-footer__link-list">\n      <li>Health Bridge Limited (t/a DrEd), 3 Angel Square, 4th Floor, 1 Torrens Street</li>\n      <li><a href="#">Help</a></li>\n      <li><a href="#">Privacy & Terms</a></li>\n    </ul>\n  </div>\n\n</footer>\n');
$templateCache.put('layout/header.html','<header class="mdl-layout__header dred-layout__header">\n  <div class="mdl-layout__header-row">\n    <!-- Title -->\n    <span class="mdl-layout-title">\n      <img src="https://www.dred.com/logo-de.png" alt="DrEd">\n    </span>\n  </div>\n</header>\n');
$templateCache.put('reviews/reviews.html','<div class="dred-layout_reviews dred-flip__card" ng-class="{flip: $ctrl.reviews.isSubmitting == true}">\n  <div class="dred-card-wide mdl-card mdl-shadow--2dp front">\n    <div class="mdl-tabs dred-tabs mdl-js-tabs mdl-js-ripple-effect">\n      <div class="mdl-tabs__tab-bar dred-tabs__tab-bar">\n        <a ng-href="#step_01" class="mdl-tabs__tab is-active">Step 1</a>\n        <a ng-href="#step_02" class="mdl-tabs__tab" ng-class="{invalid: reviews.$invalid }">Step 2</a>\n        <a ng-href="#step_03" class="mdl-tabs__tab" ng-class="{invalid: reviews.$invalid }">Step 3</a>\n      </div>\n      <list-errors errors="$ctrl.reviews.errors"></list-errors>\n      <form name="reviews" class="dred-form__reviews" novalidate>\n        <div class="mdl-tabs__panel is-active" id="step_01">\n          <div class="mdl-textfield dred-textfield mdl-js-textfield mdl-textfield--floating-label">\n            <input class="mdl-textfield__input" type="text" id="name" ng-model="$ctrl.reviews.user_name" ng-required="true">\n            <label class="mdl-textfield__label" for="name">Your name</label>\n            <span class="mdl-textfield__error">Please enter your name.</span>\n          </div>\n          <div class="mdl-textfield dred-textfield mdl-js-textfield mdl-textfield--floating-label">\n            <input class="mdl-textfield__input" type="text" id="title" ng-model="$ctrl.reviews.title" ng-required="true">\n            <label class="mdl-textfield__label" for="title">Title</label>\n            <span class="mdl-textfield__error">Please enter a title.</span>\n          </div>\n          <div class="mdl-textfield dred-textfield mdl-js-textfield mdl-textfield--floating-label">\n            <textarea class="mdl-textfield__input" type="text" rows="6" id="review" ng-model="$ctrl.reviews.review" ng-required="true"></textarea>\n            <label class="mdl-textfield__label" for="review">Review</label>\n            <span class="mdl-textfield__error">Please enter a description.</span>\n          </div>\n          <div class="mdl-textfield dred-textfield dred-rating__content mdl-js-textfield mdl-textfield--floating-label">\n            <span class="dred-rating__text">Rating: </span>\n            <ratings-start max="$ctrl.maxValue" value=\'$ctrl.reviews.rating\' hover=\'$ctrl.changeOnHover\' is-readonly=\'$ctrl.isReadonly\'></ratings-start>\n            <span class="dred-rating__text">{{$ctrl.reviews.rating}} of {{$ctrl.maxValue}}</span>\n            <input type="hidden" ng-model="$ctrl.reviews.rating">\n          </div>\n          <div class="dred-tabs__action">\n            <div class="mdl-tabs__tab-bar">\n              <a ng-href="#step_02" ng-class="{invalid: reviews.$invalid }" class="mdl-button dred-button mdl-js-button mdl-button--raised mdl-button--colored mdl-tabs__tab">Next</a>\n            </div>\n          </div>\n        </div>\n        <div class="mdl-tabs__panel" id="step_02">\n          <div class="dred-tabs__header">\n            <p>Shared in Social Networks</p>\n          </div>\n          <div class="dred-checkfield">\n            <label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="facebook">\n              <input type="checkbox" id="facebook" class="mdl-checkbox__input" ng-model="$ctrl.reviews.facebook">\n              <span class="mdl-checkbox__label">Facebook</span>\n            </label>\n          </div>\n          <div class="dred-checkfield">\n            <label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="twitter">\n              <input type="checkbox" id="twitter" class="mdl-checkbox__input" ng-model="$ctrl.reviews.twitter">\n              <span class="mdl-checkbox__label">Twitter</span>\n            </label>\n          </div>\n          <div class="dred-checkfield">\n            <label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="linkedin">\n              <input type="checkbox" id="linkedin" class="mdl-checkbox__input" ng-model="$ctrl.reviews.linkedin">\n              <span class="mdl-checkbox__label">Linkedin</span>\n            </label>\n          </div>\n          <div class="dred-tabs__action">\n            <div class="mdl-tabs__tab-bar">\n              <a ng-href="#step_03" ng-class="{invalid: reviews.$invalid }" class="mdl-button dred-button mdl-js-button mdl-button--raised mdl-button--colored mdl-tabs__tab">Next</a>\n            </div>\n          </div>\n        </div>\n        <div class="mdl-tabs__panel" id="step_03">\n          <div class="dred-review__verified-layout">\n            <strong class="dred-review__title">Preview Review</strong>\n            <div class="dred-textfield dred-rating__content">\n              <span class="dred-rating__text">Rating: </span>\n              <ratings-start max="$ctrl.maxValue" value=\'$ctrl.reviews.rating\' hover=\'$ctrl.changeOnHover\' is-readonly=\'true\'></ratings-start>\n              <span class="dred-rating__text">{{$ctrl.reviews.rating}} of {{$ctrl.maxValue}}</span>\n            </div>\n            <div class="dred-textfield__preview">\n              <h4>{{$ctrl.reviews.title}}</h4>\n            </div>\n            <div class="dred-textfield__preview">\n              <p>{{$ctrl.reviews.review}}</p>\n            </div>\n            <div class="dred-textfield__preview social">\n              <strong>Shared on:</strong>\n              <span ng-show="$ctrl.reviews.facebook == true">Facebook</span>\n              <span ng-show="$ctrl.reviews.twitter == true">Twitter</span>\n              <span ng-show="$ctrl.reviews.linkedin == true">Linkedin</span>\n            </div>\n          </div>\n          <div class="dred-tabs__action">\n            <button class="mdl-button dred-button mdl-js-button mdl-button--raised mdl-button--colored" ng-click="$ctrl.submit()" ng-disabled="$ctrl.reviews.isSubmitting == true">Publish</button>\n          </div>\n        </div>\n      </form>\n    </div>\n  </div>\n  <div class="dred-card-wide mdl-card mdl-shadow--2dp back">\n    <p>{{ ::$ctrl.reviews.success }}</p>\n  </div>\n</div>\n');
$templateCache.put('directives/ratings-start/ratings-start.html','<span ng-class="{isReadonly: isReadonly}">\n  <i ng-class="renderObj" \n  ng-repeat="renderObj in renderAry" \n  ng-click="setValue($index)" \n  ng-mouseenter="changeValue($index, changeOnHover )" > </i>\n</span>\n');}]);