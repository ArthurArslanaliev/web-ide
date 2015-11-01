(function () {

    'use strict';


    angular.module('webIde.editor')
        .service('fileService', fileService);


    function fileService() {
        var imgExtensions = ['jpg', 'png', 'gif'];

        this.isImage = isImage;

        function isImage(path) {
            var s = path.split('.');
            var ext = null;
            if (s.length) {
                ext = s.pop();
                return imgExtensions.indexOf(ext) > -1;
            }
            return false;
        }
    }

})();