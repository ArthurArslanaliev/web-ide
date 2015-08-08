(function () {

    'use strict';

    angular.module('webIde.github', [])
        .config(config)
        .controller('repositoryController', repositoryController);

    config.$inject = ['$stateProvider'];

    function config($stateProvider) {

        $stateProvider.state('repositories', {
            url: '/choose-repository',
            templateUrl: '/static/app/github/repo/choose-repository.html',
            controller: 'repositoryController'
        });
    }

    repositoryController.$inject = ['$scope'];

    function repositoryController() {

        $scope.repositories = ['awesome1', 'awesome2'];
    }

})();