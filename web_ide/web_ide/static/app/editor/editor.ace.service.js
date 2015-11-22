(function () {

    'use strict';

    angular.module('webIde.editor')
        .service('aceService', aceService);

    function aceService() {
        var modesMap = {
            'js': 'ace/mode/javascript',
            'css': 'ace/mode/css',
            'html': 'ace/mode/html',
            'json': 'ace/mode/json'
            },
            DEFAULT_MODE = 'ace/mode/text';

        this.getAceMode = getAceMode;
        this.setAceMode = setAceMode;

        this.setContent = setContent;
        this.getContent = getContent;

        function getAceMode(fileExtension) {
            if (fileExtension in modesMap) {
                return modesMap[fileExtension];
            }
            return DEFAULT_MODE;
        }

        function setAceMode(aceInstance, aceMode) {
            aceInstance.getSession().setMode(aceMode);
        }

        function setContent(aceInstance, content) {
            // set value and move cursor to the start
            aceInstance.setValue(content, -1);
        }

        function getContent(aceInstance) {
            return aceInstance.getValue();
        }
    }

})();