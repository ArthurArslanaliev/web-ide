(function () {

    'use strict';

    angular.module('webIde.editor')
        .service('aceService', aceService);

    function aceService() {
        var modesMap = {
            'js': 'ace/mode/javascript',
            'css': 'ace/mode/css'
            },
            DEFAULT_MODE = 'ace/mode/text';

        this.getAceMode = getAceMode;
        this.setAceMode = setAceMode;

        function getAceMode(fileExtension) {
            if (fileExtension in modesMap) {
                return modesMap[fileExtension];
            }
            return DEFAULT_MODE;
        }

        function setAceMode(aceInstance, aceMode) {
            aceInstance.getSession().setMode(aceMode);
        }
    }

})();