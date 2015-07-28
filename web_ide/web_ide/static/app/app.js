(function () {

    'use strict';


    angular.module('webIde', ['ui.router', 'webIde.home'])

        .config(config)
        .run(run);


    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    function config($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/state1");
    }

    run.$inject = ['$rootScope', '$state', '$stateParams'];

    function run($rootScope, $state, $stateParams) {

        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        $state.go('home');
    }

})();