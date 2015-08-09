(function () {

    'use strict';

    angular.module('webIde.github.repositories', [])
        .controller('repositoryController', repositoryController)
        .service('getRepositoriesService', getRepositoriesService);

    repositoryController.$inject = ['$scope', 'getRepositoriesService'];

    function repositoryController($scope, getRepositoriesService) {
        $scope.repositories = [];

        activate();

        function activate() {
            getRepositoriesService.getUserRepositories()
                .then(function(repositories) {
                    $scope.repositories = repositories.data;
                });
        }
    }

    getRepositoriesService.$inject = ['$http', 'webIdeConfig'];

    function getRepositoriesService($http, webIdeConfig) {

        this.getUserRepositories = getUserRepositories;

        function getUserRepositories() {
            return $http.get(webIdeConfig.APP_URL + '/github/repos/')
        }
    }

})();