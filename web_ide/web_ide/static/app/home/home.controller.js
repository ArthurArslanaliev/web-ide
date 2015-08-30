(function () {

    'use strict';


    angular.module('webIde.home')
        .controller('homeController', homeController);


    homeController.$inject = ['$rootScope', '$scope', '$window', 'GithubAuthService'];

    function homeController($rootScope, $scope, $window, GithubAuthService) {


        $scope.isUserLoggedIn = false;
        $scope.user = null;

        $scope.login = GithubAuthService.login;
        $scope.logout = logout;

        activate();

        function activate() {

            if ($rootScope.$user.userId && $rootScope.$user.userLogin) {
                $scope.isUserLoggedIn = true;
                $scope.user = $rootScope.$user;
            }
        }

        function logout() {

            GithubAuthService.logout()
                .then(function () {
                    $window.location.href = '/';
                });
        }
    }

})();