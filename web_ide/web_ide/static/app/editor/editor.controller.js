(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = [
        '$scope',
        '$stateParams',
        '$timeout',
        'editorService',
        'fileService',
        'aceService',
        'contextMenuService'
    ];

    function editorController($scope,
                              $stateParams,
                              $timeout,
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
        $scope.saveContent = saveContent;

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
                                aceService.setContent(aceEditor, atob(resp.data));
                            }
                        });
                }
            }
        }, false);

        $scope.$on('terminal-input', function (e, consoleInput) {
            var cmd = consoleInput[0];
            console.log(cmd);
            // do stuff
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
            sendToTerminal(['Welcome to <webIde>!', 'You can type your git commands here!']);
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
            contextMenuService.setCreateNewFileCallback(onCreateNewFile);
            contextMenuService.setRenameCallback(onRename);
        }

        function onCreateNewFolder($itemScope, folderName) {
            var parentPath = $itemScope.node.id;
            var targetPath = parentPath + '/' + folderName;

            editorService.createFolder(targetPath, repositoryId)
                .then(function (resp) {
                    $scope.structure = resp.data;
                });
        }

        function onCreateNewFile($itemScope, folderName) {
            var parentPath = $itemScope.node.id;
            var targetPath = parentPath + '/' + folderName;

            editorService.createNewFile(targetPath, repositoryId)
                .then(function (resp) {
                    $scope.structure = resp.data;
                });
        }

        function onRename($itemScope, newName) {
            var source = $itemScope.node.id;
            var destination = source.substr(0, source.lastIndexOf('/') + 1) + newName;

            editorService.renameEntity(repositoryId, source, destination)
                .then(function (resp) {
                    $scope.structure = resp.data;
                });
        }

        function saveContent() {
            var currentNode = $scope.browser.currentNode;
            var content = aceService.getContent(aceEditor);
            var base64 = btoa(content);
            editorService.saveContent(currentNode.id, base64)
                .then(function (resp) {
                    console.log(resp.data);
                });
        }

        function sendToTerminal(text) {
            $timeout(function () {
                $scope.$broadcast('terminal-output', {
                    output: true,
                    text: text,
                    breakLine: true
                });
            });
        }
    }

})();