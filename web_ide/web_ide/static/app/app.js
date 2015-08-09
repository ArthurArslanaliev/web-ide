(function () {

    'use strict';

    angular.module('webIde', [
        'ui.router',

        'webIde.home',
        'webIde.github',
        'webIde.github.repositories'
    ])

        .config(config)
        .run(run);


    config.$inject = ['$urlRouterProvider', '$stateProvider'];

    function config($urlRouterProvider, $stateProvider) {

        $urlRouterProvider.otherwise('/state1');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/app/home/home.html',
                controller: 'homeController'
            })
            .state('repositories', {
                url: '/choose-repository',
                templateUrl: '/static/app/github/repositories/choose-repository.html',
                controller: 'repositoryController'
            });
    }

    run.$inject = ['$rootScope', '$state', '$stateParams', 'webIdeConfig'];

    function run($rootScope, $state, $stateParams, webIdeConfig) {

        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        $rootScope.$user = {
            userLogin: webIdeConfig.USER_LOGIN,
            userId: webIdeConfig.USER_ID
        };

        $state.go('home');
    }

})();