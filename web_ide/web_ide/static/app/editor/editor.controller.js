(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = ['$scope', '$stateParams', 'editorService'];

    function editorController($scope, $stateParams, editorService) {

        activate();

        $scope.structure = [];

        $scope.$watch('structure.currentNode', function (newObj, oldObj) {
            if ($scope.structure && angular.isObject($scope.structure.currentNode)) {
                console.log($scope.structure.currentNode.id);
            }
        }, false);

        function activate() {

            editorService.loadEditor($stateParams.repo)
                .then(function (resp) {
                    return resp.data.id;
                })
                .then(editorService.loadRepositoryStructure)
                .then(function (resp) {
                    $scope.structure = resp.data;
                })
        }
    }

})();