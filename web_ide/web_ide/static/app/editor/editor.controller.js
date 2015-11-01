(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = ['$scope', '$stateParams', 'editorService', 'fileService'];

    function editorController($scope, $stateParams, editorService, fileService) {

        $scope.structure = [];
        $scope.content = null;
        $scope.showCodeEditor = true;
        $scope.image = null;

        activate();

        $scope.$watch('browser.currentNode', function (newObj, oldObj) {
            if ($scope.browser && angular.isObject($scope.browser.currentNode)) {
                var selectedNode = $scope.browser.currentNode;
                if (!selectedNode.children) {
                    editorService.getContent(selectedNode.id)
                        .then(function (resp) {
                            if (fileService.isImage(selectedNode.id)) {
                                $scope.image = 'data:image/png;base64, ' + resp.data;
                                $scope.showCodeEditor = false;
                            } else {
                                $scope.showCodeEditor = true;
                                $scope.content = atob(resp.data);
                            }
                        });
                }
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