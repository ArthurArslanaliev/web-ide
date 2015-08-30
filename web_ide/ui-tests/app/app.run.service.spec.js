describe('test app.run.service', function () {

    'use strict';


    var expectedState = 'test',
        expectedUserId = 'testUserId',
        expectedUserLogin = 'testUserLogin',
        $stateMock = null;

    beforeEach(module('webIde'));

    beforeEach(function () {

        $stateMock = {
            state: expectedState,
            go: function () {
            }
        };

        spyOn($stateMock, 'go');

        module(function ($provide) {
            $provide.value('webIdeConfig', {
                USER_LOGIN: expectedUserLogin,
                USER_ID: expectedUserId
            });
            $provide.value('$state', $stateMock);
            $provide.value('$stateParams', {
                state: expectedState
            });
        });
    });

    it('should initialize $rootScope with values', inject(function (runService, $rootScope) {

        runService.run();

        expect($rootScope.$state.state).toBe(expectedState);
        expect($rootScope.$stateParams.state).toBe(expectedState);
        expect($rootScope.$user).toEqual({
            userLogin: expectedUserLogin,
            userId: expectedUserId
        });
        expect($stateMock.go).toHaveBeenCalledWith('home');
    }));
});