(function() {
    'use strict';


    angular.module('webIde.github')

        .service('GithubAuthService', GithubAuthService);


    GithubAuthService.$inject = ['$http', '$window', 'webIdeConfig'];

    function GithubAuthService($http, $window, webIdeConfig) {

        this.login = function() {

            $window.location.href = webIdeConfig.APP_URL + '/github/auth';
        };

        this.logout = function() {
            return $http.post(webIdeConfig.APP_URL + '/github/logout')
        };
    }

})();