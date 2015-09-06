(function () {

    'use strict';


    angular.module('webIde.github.repository')
        .controller('repositoryController', repositoryController);

    repositoryController.$inject = ['$scope', 'getRepositoriesService'];

    function repositoryController($scope, getRepositoriesService) {

        $scope.repositories = [];
        $scope.chosen = null;

        $scope.choose = choose;
        $scope.isMeChosen = isMeChosen;
        $scope.loadWebIde = loadWebIde;

        activate();

        function activate() {

            getRepositoriesService.getUserRepositories()
                .then(function (repositories) {
                    console.log(repositories);

                    $scope.repositories = repositories.data;
                });
        }

        function isMeChosen(repo) {

            return $scope.chosen && $scope.chosen.id === repo.id;
        }

        function choose(repo) {

            $scope.chosen = repo;
        }

        function loadWebIde() {
            alert('loading webIde');
        }
    }

})();