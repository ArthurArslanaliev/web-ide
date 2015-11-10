(function () {

    'use strict';


    angular.module('webIde', [
        'ui.router',
        'ui.ace',
        'angularTreeview',
        'ui.bootstrap.contextMenu',
        'vtortola.ng-terminal',
        'ui.bootstrap',

        'webIde.home',
        'webIde.github',
        'webIde.github.repository',
        'webIde.editor'
    ]);

})();