(function () {

    'use strict';


    angular.module('webIde')
        .run(run);

    run.$inject = ['$rootScope', '$state', '$stateParams', 'webIdeConfig'];

    function run($rootScope, $state, $stateParams, webIdeConfig) {

        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        $rootScope.$user = {
            userLogin: webIdeConfig.USER_LOGIN,
            userId: webIdeConfig.USER_ID
        };

        $state.go('home');
    }

})();