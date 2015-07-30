(function () {
    'use strict';


    angular.module('webIde.home', ['webIde.github'])

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

    homeController.$inject = ['$rootScope', '$scope', 'GithubAuthService'];

    function homeController($rootScope, $scope, GithubAuthService) {
        $scope.isUserLoggedIn = false;
        $scope.user = null;

        $scope.login = GithubAuthService.login;
        $scope.logout = null;

        activate();

        function activate() {
            if ($rootScope.$user) {
                $scope.isUserLoggedIn = true;
                $scope.user = $rootScope.$user;
            }
        }
    }

})();