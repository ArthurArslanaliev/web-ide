(function () {

    'use strict';


    angular.module('webIde', ['ui.router', 'webIde.home', 'webIde.github'])

        .config(config)
        .run(run);


    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    function config($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/state1");
    }

    run.$inject = ['$rootScope', '$state', '$stateParams', 'webIdeConfig'];

    function run($rootScope, $state, $stateParams, webIdeConfig) {

        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        $rootScope.$user = {
            userName: webIdeConfig.USER_NAME,
            email: webIdeConfig.USER_EMAIL
        };

        $state.go('home');
    }

})();