(function () {

    'use strict';


    angular.module('webIde', [
        'ui.router',
        'ngMock',

        'webIde.home',
        'webIde.github',
        'webIde.github.repository'
    ]);

})();