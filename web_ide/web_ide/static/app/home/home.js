(function () {
    'use strict';


    angular.module('webIde.home', [])

        .config(config);


    config.$inject = ['$stateProvider'];

    function config($stateProvider) {

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/app/home/home.html',
                controller: homeController
            })
    }

    homeController.$inject = ['$scope'];

    function homeController($scope) {

    }

})();