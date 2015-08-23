describe('test home.controller', function () {

    'use strict';

    var ctrl = null,
        scope = null,
        githubAuthServiceMock = null,
        $window = null,
        expectedUserId = 'testUserId',
        expectedUserLogin = 'testUserLogin';

    beforeEach(module('webIde.home'));

    beforeEach(inject(function ($controller) {
        var $rootScope = {
            $user: {
                userId: expectedUserId,
                userLogin: expectedUserLogin
            }
        };
        scope = {};
        githubAuthServiceMock = {
            login: function () {
            },
            logout: function () {
            }
        };
        $window = {
            location: {
                href: 'base'
            }
        };

        spyOn(githubAuthServiceMock, 'login');

        ctrl = $controller('homeController', {
            $rootScope: $rootScope,
            $scope: scope,
            $window: $window,
            GithubAuthService: githubAuthServiceMock
        })
    }));

    it('should initialize $scope', function () {
        expect(scope.isUserLoggedIn).toBe(true);
        expect(scope.user.userId).toBe(expectedUserId);
        expect(scope.user.userLogin).toBe(expectedUserLogin);
    });

    it('should call github.auth.service login', function () {

        scope.login();

        expect(githubAuthServiceMock.login).toHaveBeenCalled();
    });
});

