(function () {

    'use strict';


    angular.module('webIde')
        .run(run);

    run.$inject = ['runService'];

    function run(runService) {

        runService.run();
    }

})();