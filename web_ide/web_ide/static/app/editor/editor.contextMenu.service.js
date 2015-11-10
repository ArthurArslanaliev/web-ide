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
            onCreateNewFolder = null;

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
            }
        ];
        var rename = [
            RENAME,
            function ($itemScope) {
                var modal = openNewEntityModal(RENAME);
            }
        ];
        var deleteOpt = [
            DELETE,
            function ($itemScope) {
                // Show confirmation modal
            }
        ];


        this.getContextMenu = getContextMenu;
        this.setCreateNewFolderCallback = setCreateNewFolderCallBack;

        function getContextMenu(item) {
            var menuOpt = [];
            if (item.children) {
                menuOpt.push(createNewFolder);
                menuOpt.push(createNewFile);
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
    }

})();