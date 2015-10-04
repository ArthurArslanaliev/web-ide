(function () {

    'use strict';


    angular.module('webIde.editor')
        .service('editorService', editorService);

    editorService.$inject = ['$http', 'webIdeConfig'];

    function editorService($http, webIdeConfig) {

        this.loadEditor = loadEditor;

        function loadEditor(repositoryName) {

            return $http.post(webIdeConfig.APP_URL + '/github/repos/' + repositoryName);
        }
    }
    
})();