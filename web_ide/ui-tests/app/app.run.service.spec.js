describe('test app.run.service', function () {

    'use strict';


    var expectedState = 'test',
        expectedUserId = 'testUserId',
        expectedUserLogin = 'testUserLogin',
        $stateMock = null;

    beforeEach(module('webIde'));

    beforeEach(function () {

        var webIdeConfigMock = {
            USER_LOGIN: expectedUserLogin,
            USER_ID: expectedUserId
        };

        $stateMock = {
            state: expectedState,
            go: function () {
            }
        };

        spyOn($stateMock, 'go');

        var $stateParamsMock = {
            state: expectedState
        };

        module(function ($provide) {
            $provide.value('webIdeConfig', webIdeConfigMock);
            $provide.value('$state', $stateMock);
            $provide.value('$stateParams', $stateParamsMock);
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