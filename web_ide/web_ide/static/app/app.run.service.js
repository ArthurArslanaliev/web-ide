(function () {

    'use strict';


    angular.module('webIde')
        .service('runService', runService);

    runService.$inject = ['$rootScope', '$state', '$stateParams', 'webIdeConfig'];

    function runService($rootScope, $state, $stateParams, webIdeConfig) {

        this.run = run;

        function run() {

            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;

            $rootScope.$user = {
                userLogin: webIdeConfig.USER_LOGIN,
                userId: webIdeConfig.USER_ID
            };

            $state.go('home');
        }
    }

})();