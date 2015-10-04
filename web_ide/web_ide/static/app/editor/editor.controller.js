(function () {

    'use strict';


    angular.module('webIde.editor')
        .controller('editorController', editorController);

    editorController.$inject = ['$scope', '$stateParams', 'editorService'];

    function editorController($scope, $stateParams, editorService) {

        activate();

        function activate() {

            editorService.loadEditor($stateParams.repo)
                .then(function (resp) {
                    console.log(resp);
                });

        }
    }

})();