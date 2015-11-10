(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorNewEntityModalCtrl', editorNewEntityModalCtrl);

    editorNewEntityModalCtrl.$inject = ['$scope', '$uibModalInstance', 'title'];

    function editorNewEntityModalCtrl($scope, $uibModalInstance, title) {

        $scope.newEntityName = null;

        $scope.title = title;
        $scope.ok = ok;
        $scope.cancel = cancel;

        function ok() {
            $uibModalInstance.close($scope.newEntityName);
        }

        function cancel() {
            $uibModalInstance.dismiss('cancel');
        }
    }
})();