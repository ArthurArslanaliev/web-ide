(function () {

    'use strict';

    angular.module('webIde.editor')
        .service('contextMenuService', contextMenuService);

    contextMenuService.$inject = ['$uibModal'];

    function contextMenuService($uibModal) {
        var CREATE_NEW_FOLDER = 'Create New Folder',
            CREATE_NEW_FILE = 'Create New Fille',
            RENAME = 'Rename',
            DELETE = 'Delete',
            onCreateNewFolder = null,
            onCreateNewFile = null,
            onRename = null;

        var createNewFolder = [
            CREATE_NEW_FOLDER,

            function ($itemScope) {
                var modal = openNewEntityModal(CREATE_NEW_FOLDER);
                modal.result.then(function (newEntityName) {
                    onCreateNewFolder($itemScope, newEntityName);
                });
            }
        ];
        var createNewFile = [
            CREATE_NEW_FILE,

            function ($itemScope) {
                var modal = openNewEntityModal(CREATE_NEW_FILE);
                modal.result.then(function (newEntityName) {
                    onCreateNewFile($itemScope, newEntityName);
                });
            }
        ];
        var rename = [
            RENAME,

            function ($itemScope) {
                var title = $itemScope.node.children ? 'New name for folder' :
                    'New name for file';

                var modal = openNewEntityModal(title);
                modal.result.then(function (newEntityName) {
                    onRename($itemScope, newEntityName);
                });
            }
        ];
        var deleteOpt = [
            DELETE,

            function ($itemScope) {
                // Show confirmation modal
            }
        ];
        var run = [
            'Preview',

            function ($itemScope) {
                var path = '/preview/' + $itemScope.node.id;
                window.open(path, '_blank');
            }
        ];


        this.getContextMenu = getContextMenu;
        this.setCreateNewFolderCallback = setCreateNewFolderCallBack;
        this.setCreateNewFileCallback = setCreateNewFileCallback;
        this.setRenameCallback = setRenameCallback;

        function getContextMenu(item) {
            var menuOpt = [];
            if (item.children) {
                menuOpt.push(createNewFolder);
                menuOpt.push(createNewFile);
            } else {
                menuOpt.push(run);
            }
            menuOpt.push(rename);
            menuOpt.push(deleteOpt);
            return menuOpt;
        }

        function openNewEntityModal(title) {
            return $uibModal.open({
                animation: true,
                templateUrl: '/static/app/editor/newEntityModal.html',
                controller: 'editorNewEntityModalCtrl',
                size: 'sm',
                resolve: {
                    title: function () {
                        return title;
                    }
                }
            });
        }

        function setCreateNewFolderCallBack(callback) {
            onCreateNewFolder = callback;
        }

        function setCreateNewFileCallback(callback) {
            onCreateNewFile = callback;
        }

        function setRenameCallback(callback) {
            onRename = callback;
        }
    }

})();