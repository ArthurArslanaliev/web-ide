(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = [
        '$scope',
        '$stateParams',
        'editorService',
        'fileService',
        'aceService',
        'contextMenuService'
    ];

    function editorController($scope,
                              $stateParams,
                              editorService,
                              fileService,
                              aceService,
                              contextMenuService) {

        var aceEditor,
            repositoryId;

        $scope.structure = [];
        $scope.content = null;
        $scope.showCodeEditor = true;
        $scope.image = null;

        $scope.showContextMenu = showContextMenu;

        $scope.aceOptions = {
            onLoad: aceOnLoad
        };

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
                                var fileExtension = fileService.getFileExtension(selectedNode.id);
                                var aceMode = aceService.getAceMode(fileExtension);
                                aceService.setAceMode(aceEditor, aceMode);

                                $scope.showCodeEditor = true;
                                $scope.content = atob(resp.data);
                            }
                        });
                }
            }
        }, false);

        $scope.$broadcast('terminal-output', {
            output: true,
            text: ['Welcome to vtortola.GitHub.io',
                'This is an example of ng-terminal-emulator.',
                '',
                "Please type 'help' to open a list of commands"],
            breakLine: true
        });

        function activate() {

            editorService.loadEditor($stateParams.repo)
                .then(function (resp) {
                    repositoryId = resp.data.id;
                    return repositoryId;
                })
                .then(editorService.loadRepositoryStructure)
                .then(function (resp) {
                    $scope.structure = resp.data;
                });

            setContextMenuCallbacks();
        }

        function aceOnLoad(_ace) {
            aceEditor = _ace;
        }

        function showContextMenu(item) {
            var itemId = item.id;
            var selectedNode = $scope.browser.currentNode;
            if (itemId && angular.isObject(selectedNode) && selectedNode.id === itemId) {
                return contextMenuService.getContextMenu(item);
            }
            return [];
        }

        function setContextMenuCallbacks() {
            contextMenuService.setCreateNewFolderCallback(onCreateNewFolder);
        }

        function onCreateNewFolder($itemScope, folderName) {
            var parentPath = $itemScope.node.id;
            var targetPath = parentPath + '/' + folderName;

            editorService.createFolder(targetPath, repositoryId)
                .then(function (resp) {
                    console.log(resp.data);
                    $scope.structure = resp.data;
                });
        }
    }

})();