(function () {

    'use strict';


    angular.module('webIde')
        .config(config);

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
                templateUrl: '/static/app/github/repository/choose-repository.html',
                controller: 'repositoryController'
            })
            .state('editor', {
                url: '/editor/:repo',
                templateUrl: '/static/app/editor/editor.html',
                controller: 'editorController'
            })
    }

})();