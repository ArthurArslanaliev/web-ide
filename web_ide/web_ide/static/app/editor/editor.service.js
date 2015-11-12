(function () {

    'use strict';


    angular.module('webIde.editor')
        .service('editorService', editorService);

    editorService.$inject = ['$http', 'webIdeConfig'];

    function editorService($http, webIdeConfig) {

        this.loadEditor = loadEditor;
        this.loadRepositoryStructure = loadRepositoryStructure;
        this.getContent = getContent;
        this.createFolder = createFolder;
        this.createNewFile = createNewFile;
        this.saveContent = saveContent;

        function loadEditor(repositoryName) {
            return $http.post(webIdeConfig.APP_URL + '/github/repos/' + repositoryName);
        }

        function loadRepositoryStructure(repositoryId) {
            return $http.get(webIdeConfig.APP_URL + '/repository/structure/' + repositoryId);
        }

        function getContent(path) {
            return $http.get(webIdeConfig.APP_URL + '/repository/content?path=' + path)
        }

        function createFolder(path, repositoryId) {
            var data = {path: path, type: 'folder'};
            return $http.post(webIdeConfig.APP_URL + '/repository/structure/' + repositoryId + '/create/', data);
        }

        function createNewFile(path, repositoryId) {
            var data = {path: path, type: 'file'};
            return $http.post(webIdeConfig.APP_URL + '/repository/structure/' + repositoryId + '/create/', data);
        }

        function saveContent(path, content) {
            var data = {path: path, content: content};
            return $http.put(webIdeConfig.APP_URL + '/repository/content/', data);
        }
    }

})();