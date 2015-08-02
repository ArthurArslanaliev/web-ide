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
            userLogin: webIdeConfig.USER_ID,
            userId: webIdeConfig.USER_LOGIN
        };

        $state.go('home');
    }

})();