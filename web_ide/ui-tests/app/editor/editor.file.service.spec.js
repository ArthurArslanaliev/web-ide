describe('test webIde.editor.fileService', function () {

    'use strict';

    beforeEach(module('webIde.editor'));

    it('should detect image files', inject(function (fileService) {

        expect(fileService.isImage('/directory/another_one/image.png')).toBe(true);
        expect(fileService.isImage('/directory/another_one/image.jpg')).toBe(true);
        expect(fileService.isImage('/image.gif')).toBe(true);

        expect(fileService.isImage('/directory/another_one/')).toBe(false);
        expect(fileService.isImage('/directory/another_one/file.awesome.js')).toBe(false);
        expect(fileService.isImage('/directory/another_one/javascript.js')).toBe(false);
    }));
});