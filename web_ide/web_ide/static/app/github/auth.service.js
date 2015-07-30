(function() {
    'use strict';


    angular.module('webIde.github')

        .service('GithubAuthService', GithubAuthService);


    GithubAuthService.$inject = ['$window', 'webIdeConfig'];

    function GithubAuthService($window, webIdeConfig) {

        this.login = function() {

            $window.location.href = webIdeConfig.APP_URL + '/github/auth';
        };

        this.logout = function() {

        };
    }

})();