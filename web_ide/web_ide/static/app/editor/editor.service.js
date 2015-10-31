(function () {

    'use strict';


    angular.module('webIde.editor')
        .service('editorService', editorService);

    editorService.$inject = ['$http', 'webIdeConfig'];

    function editorService($http, webIdeConfig) {

        this.loadEditor = loadEditor;
        this.loadRepositoryStructure = loadRepositoryStructure;

        function loadEditor(repositoryName) {
            return $http.post(webIdeConfig.APP_URL + '/github/repos/' + repositoryName);
        }

        function loadRepositoryStructure(repositoryId) {
            return $http.get(webIdeConfig.APP_URL + '/repository/structure/' + repositoryId);
        }
    }
    
})();