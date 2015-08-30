(function () {

    'use strict';


    angular.module('webIde', [
        'ui.router',

        'webIde.home',
        'webIde.github',
        'webIde.github.repository'
    ]);

})();