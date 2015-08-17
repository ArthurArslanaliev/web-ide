(function (){

    'use strict';


    angular.module('webIde.github.repository')
        .service('getRepositoriesService');

    getRepositoriesService.$inject = ['$http', 'webIdeConfig'];

    function getRepositoriesService($http, webIdeConfig) {

        this.getUserRepositories = getUserRepositories;

        function getUserRepositories() {
            return $http.get(webIdeConfig.APP_URL + '/github/repos/')
        }
    }

})();