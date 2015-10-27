(function () {

    'use strict';


    angular.module('webIde', [
        'ui.router',
        'angularTreeview',

        'webIde.home',
        'webIde.github',
        'webIde.github.repository',
        'webIde.editor'
    ]);

})();