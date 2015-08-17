(function () {

    'use strict';


    angular.module('webIde.github.repository')
        .controller('repositoryController', repositoryController);

    repositoryController.$inject = ['$scope', 'getRepositoriesService'];

    function repositoryController($scope, getRepositoriesService) {
        $scope.repositories = [];

        activate();

        function activate() {
            getRepositoriesService.getUserRepositories()
                .then(function (repositories) {
                    $scope.repositories = repositories.data;
                });
        }
    }

})();