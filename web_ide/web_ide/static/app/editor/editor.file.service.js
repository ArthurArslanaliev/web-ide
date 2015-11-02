(function () {

    'use strict';


    angular.module('webIde.editor')
        .service('fileService', fileService);


    function fileService() {
        var imgExtensions = ['jpg', 'png', 'gif'];

        this.isImage = isImage;
        this.getFileExtension = getFileExtension;

        function isImage(path) {
            var ext = getFileExtension(path);
            return ext && imgExtensions.indexOf(ext) > -1;
        }

        function getFileExtension(path) {
            var s = path.split('.');
            if (s.length) {
                return s.pop();
            }
            return null;
        }
    }

})();