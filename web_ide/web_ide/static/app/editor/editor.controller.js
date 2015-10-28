(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = ['$scope', '$stateParams', 'editorService'];

    function editorController($scope, $stateParams, editorService) {

        activate();

        $scope.treedata = [
            {
                "label": "User", "id": "role1", "children": [
                {"label": "subUser1", "id": "role11", "children": []},
                {
                    "label": "subUser2", "id": "role12", "children": [
                    {
                        "label": "subUser2-1", "id": "role121", "children": [
                        {"label": "subUser2-1-1", "id": "role1211", "children": []},
                        {"label": "subUser2-1-2", "id": "role1212", "children": []}
                    ]
                    }
                ]
                }
            ]
            },
            {"label": "Admin", "id": "role2", "children": []},
            {"label": "Guest", "id": "role3", "children": []}
        ];

        $scope.$watch('abc.currentNode', function (newObj, oldObj) {
            if ($scope.abc && angular.isObject($scope.abc.currentNode)) {
                console.log('Node Selected!!');
                console.log($scope.abc.currentNode);
            }
        }, false);

        function activate() {

            editorService.loadEditor($stateParams.repo)
                .then(function (resp) {
                    console.log(resp);
                });

        }
    }

})();