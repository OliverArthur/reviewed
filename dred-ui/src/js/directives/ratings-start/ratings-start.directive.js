export default class RatingsStartDirective {
  constructor() {
    'ngInject';

    this.restrict = 'EA',
      this.scope = {
        'value': '=value',
        'max': '=max',
        'hover': '=hover',
        'isReadonly': '=isReadonly'
      },
      this.templateUrl = 'directives/ratings-start/ratings-start.html',
      this.replace = true
  }

  link(scope, element, attrs, ctrl) {
    function renderValue() {
      scope.renderAry = [];
      for (let i = 0; i < scope.max; i++) {
        if (i < scope.value) {
          scope.renderAry.push({
            'fa fa-star fa-2x': true
          });
        } else {
          scope.renderAry.push({
            'fa fa-star-o fa-2x': true
          });
        }
      }
    }

    if (scope.max === undefined) scope.max = 5; // default

    scope.$watch('value', (newValue, oldValue) => {
      if (newValue) {

        renderValue();
      }
    });

    scope.$watch('max', (newValue, oldValue) => {
      if (newValue) {
        console.log(newValue);
        renderValue();
      }
    });

    scope.setValue = index => {
      if (!scope.isReadonly && scope.isReadonly !== undefined) {
        scope.value = index + 1;
      }
    };

    scope.changeValue = index => {
      if (scope.hover) {
        scope.setValue(index);
      }
    };
  }
};
